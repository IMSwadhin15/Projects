/* Modified version of the code.cpp file, with using structure, user input and other updates*/


#include <bits/stdc++.h>
#include <filesystem>
#include <fstream>

using namespace std;
namespace fs = std::filesystem;

static const unordered_map<string, float> Grade_points = 
{
    {"O", 10.0}, {"E", 9.0}, {"A", 8.0},
    {"B", 7.0}, {"C", 6.0}, {"D", 5.0},
    {"F", 0.0}
};

// this is not a global declaration but only a format which will be used further.
struct GPAresult{
    double gpa = 0.0;
    double credits = 0.0;
    bool failed = false;
};

// struct used in place of any other datatype, because we have to return multiple results
GPAresult calculate_gpa(fs::path file_path){
    
    //ifstream is used for file opening, so no need of file open codes
    ifstream file(file_path);

    // check if file is opened or not
    if(!file){
        cout << "Error opening:" << file_path << endl;
        return {};
    }

    string line;
    // skip the first line
    getline(file, line);

    double total_grade_points = 0.0, total_credits = 0.0;
    bool failed = false;

    while(getline(file, line)){
        
        if(line.empty()) continue; // skip if the line is empty

        stringstream ss(line); // break the single string to stringstream
        string word;
        vector<string> col;

        while(getline(ss, word, ',')){
            col.push_back(word);
        }

        // check if the col size is 4, becoz csv is a not very strict about the col nos
        if(col.size() < 4) continue;

        // get grade from the row
        string grade = col[3];

        // remove if space at the end of the line
        grade.erase(remove_if(grade.begin(), grade.end(), ::isspace), grade.end());

        // extract the credit of the subject and convert it to no from string
        double credits = stod(col[2]);

        auto it = Grade_points.find(grade);
        if(it != Grade_points.end()){
            if(grade == "F") failed = true;
            total_grade_points += it->second * credits;
            total_credits += credits;
        }
        
    }

    GPAresult result;
    result.credits = total_credits;
    result.failed = failed;

    if(total_credits > 0) result.gpa = total_grade_points/total_credits;

    return result;
    
}

int main(int argc, char* argv[]){
    
    // argc < 2 means only the function is there, no input
    if (argc < 2){
        cout << "Error in giving user input" << endl;
        return 1;
    }

    // USER INPUT
    // if argc is = 2, means input path is there
    // argv[0] is for the function
    fs::path folder_path = argv[1];

    // check for invalid folder path
    // if path not exists or folder not exist
    if(!fs::exists(folder_path) || !fs::is_directory(folder_path)){
        cout << "Invalid folder path" << endl;
        return 1;
    }

    double temp_gpa = 0.0, total_credits = 0.0;
    bool any_fail = false;

    // FOLDER TRAVERSE
    for(const auto& entry : fs::directory_iterator(folder_path)){
        if (entry.path().extension() == ".csv") // check if it is file and if have .csv extension
        {
            GPAresult result = calculate_gpa(entry.path()); // pass the path to calculate the individual gpas
            temp_gpa += result.gpa * result.credits;
            total_credits += result.credits;
            any_fail |= result.failed; // this will do bit or operation
        }

    }

    if(total_credits == 0){
        cout << "no valid data found" << endl;
        return 1;
    }

    double cgpa = temp_gpa / total_credits;
    std::cout << "CGPA: " << std::fixed << std::setprecision(2) << cgpa << "\n";
    std::cout << (any_fail ? "Failed\n" : "Passed\n");

    return 0;
    
}
