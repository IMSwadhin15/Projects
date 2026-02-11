#include <bits/stdc++.h>
#include <filesystem>
#include <fstream>
#include <iomanip>

using namespace std;

// from now fs:: will be written inplace of std::filesystem::
namespace fs = std::filesystem;

int fail_flag = 0;

pair<double, double> calculate_gpa(fs::path file_path){

    // grades to grade points table
    unordered_map<string, double> grade_points = {
        {"O", 10.0},
        {"E", 9.0},
        {"A", 8.0},
        {"B", 7.0},
        {"C", 6.0},
        {"D", 5.0},
        {"F", 0.0},
    };


    fstream file;
    file.open(file_path, ios::in);
    
    if (!file.is_open()) {
        cerr << "Error opening file!" << endl;
        return {0.0, 0.0};
    }

    string line, word;
    vector<string> row;
    double total_grade_points = 0.0, total_credits = 0.0, gpa = 0.0;

    // Skip header
    getline(file, line);

    while(getline(file, line)){

        if(line.empty()) continue;

        stringstream s(line);

        while(getline(s, word, ',')){
            row.push_back(word);
        }

        string grade = row[3];
        double credit = stod(row[2]);

        grade.erase(remove_if(grade.begin(), grade.end(), ::isspace), grade.end());

        if(grade_points.find(grade) != grade_points.end()){
            if(grade == "F") fail_flag = 1;
            total_grade_points += grade_points[grade] * credit;
            total_credits += credit;
        }
        row.clear();
    }
    
    file.close();

    if (total_credits == 0.0) {
        return {0.0, 0.0};
    }

    gpa = total_grade_points / total_credits;
    return {gpa, total_credits};
}


int main(){
    double cgpa = 0.0, total_credits=0.0,temp_gpa=0.0;

    fs::path folder_path = "D:\\x\\Swadhin\\cpp\\CGPA_Calculator\\Swadhin_21011177";

    if(!fs::exists(folder_path) || !fs::is_directory(folder_path)){
        cout << "Folder not exists" << endl;
    }
    else{
        for(const auto& entry : fs::directory_iterator(folder_path)){
            if(fs::is_regular_file(entry.path()) && entry.path().extension() == ".csv"){
                fs::path file_path = entry.path();
                // calculate gpa of each file
                auto[gpa, credits_per_sem] = calculate_gpa(file_path);
                temp_gpa = temp_gpa + (gpa * credits_per_sem);
                total_credits = total_credits + credits_per_sem;
            }
        }

        cgpa = temp_gpa / total_credits;
        cout << "CGPA: " << fixed << setprecision(2) << cgpa << endl;
        if(fail_flag == 1) cout << "Failed";
        else cout << "Passed";
    }
    return 0;
}
