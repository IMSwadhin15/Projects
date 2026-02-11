#include <bits/stdc++.h>
#include <filesystem>
#include <fstream>

using namespace std;

namespace fs = std::filesystem;

// only a value holder, with the default values
struct GPAresult{
    double credits = 0.0;
    double gpa = 0.0;
    bool failed = false;
};

/* class store the grade points details*/
class Subject{
protected:
    unordered_map<string, int> grade_points = {
        {"O",10},{"E",9},{"A",8},{"B",7},{"C",6},{"D",5},{"F",0}
    };

};

class Semester : public Subject{
public:
    GPAresult gpa_calculate(fs::path file_path){
        // check if it is file or not
        ifstream file(file_path);
        if(!file){
            cout << "error opening" << file_path << endl;
            return {};
        }
        
        double total_credits = 0.0, total_grade_points = 0.0;
        bool failed = false;
        string line;
        getline(file, line); // skip header

        while(getline(file, line)){
            if(line.empty()) continue;

            stringstream ss(line);
            string word;
            vector<string> col;

            while(getline(ss,word,',')){
                col.push_back(word);
            }

            if(col.size() < 3) continue;

            string grade = col[3];
            double credits = stod(col[2]);
            // remove space with grade character
            grade.erase(remove_if(grade.begin(), grade.end(), ::isspace), grade.end());
            
            auto it = grade_points.find(grade);
            if(it != grade_points.end()){
                if(grade == "F") failed = true;
                total_grade_points += credits * it->second;
                total_credits += credits;
            }
        }

        GPAresult res;
        res.credits = total_credits;
        res.failed = failed;

        if(total_credits > 0) res.gpa = total_grade_points / total_credits;

        return res;
    }
};

class Student{
    // by default private
    fs::path folder_path;
    double temp_gpa = 0.0, cgpa = 0.0, total_credits = 0.0;
    bool is_fail = false;

public:
    // Constructor
    Student(fs::path folder_path){
        this -> folder_path = folder_path;
    }

    void calculate_cgpa(){
        Semester sem;
        // Traverse the folder
        for(const auto& entry : fs::directory_iterator(folder_path)){
            if(entry.path().extension() == ".csv"){ /* check if it is a file that is with csv extension or not*/
                GPAresult result = sem.gpa_calculate(entry.path());
                temp_gpa += result.gpa * result.credits;
                total_credits += result.credits;
                is_fail |= result.failed;
            }
        }

        if(total_credits == 0) {
            cout << "no valid result found";
            return;
        }

        cgpa = temp_gpa / total_credits;
        cout << "final cgpa: " << cgpa << endl;
        if(is_fail) cout << "Failed" << endl;
        else cout << "Passed" << endl;
    }


};

int main(int argc, char* argv[]){

    if(argc < 2){
        cout << "Error in giving user input" << endl;
        return 1;
    }

    fs::path folder_path = argv[1];

    // check if the folder is there
    if(!fs::exists(folder_path) || !fs::is_directory(folder_path)){
        cout << "Path is incorrect or No folder there" << endl;
        return 1;
    }

    Student s(folder_path); // folder path passed to the student constructor
    s.calculate_cgpa();

}