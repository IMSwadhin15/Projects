#include <bits/stdc++.h>
#include <cstdlib>
#include <ctime>

using namespace std;

class Casino{
    private:
    string name;
    int amount = 0;

    public:
    void setName(){
        cout << "Player Enter Name: " << endl;
        cin >> name;
        
    }

    void setAmount(){
        int amt;
        while(1){
            cout << "Player Enter Balance: " << endl;
            cin >> amt;

            
            if(amt + amount >= 1000) break;
            else cout << "WARNING: Minimum Balance atleat 1000 rupees" << endl;
        }
        amount = amt + amount;
        TotalAmount();
        }

    void showRules(){
        cout << "RULES TO FOLLOW" << endl;
        cout << "1.Minimum total amount is 1000 rupees." << endl;
        cout << "2.Minimum bet amount and denomination is 500 rupees." << endl;
        cout << "3.Player have to guess a number in between 1 to 10, inclusive." << endl;
        cout << "4.With each win the player got the FIVE TIMES of the amount betted." << endl;
        cout << "5.With each loss, player will loose the betted amount." << endl;
        cout << "6.When the total amount will reach below thousand rupees, player will lost the match." << endl;
        cout << "7.After the result of each bet, player have the choice to exit with the current amount." << endl;
        cout << "-----------------------------------------------------------------------------------------" << endl;
    }

    void TotalAmount(){
        cout << "Your Current amount is: "<< amount << endl;
    }

    void menu(){
        cout << "1. Bet Again to get FIVE TIMES PROFIT." << endl;
        cout << "2. Exit with your current total balance." << endl;
        cout << "0. To see rules again." << endl;
    }

    void exit_from_game(){
        cout << "Withdrwing Balance " << amount << endl;
        cout << "-------------------- GAME OVER --------------------" << endl;
        exit(0);
    }

    void GameLoop(){
        int betAmount, GuessNumber, RandomNumber; 
        srand(time(0)); //this is the seed to change numbers everytime
        while(1){
            cout << "Place the bet amount" << endl;
            cin >> betAmount;

            if(betAmount < 500 || betAmount % 500 != 0){
                cout << "Bet Amount not satisfied the requirement. Bet AGAIN" << endl;
                continue;
            }

            cout << "Guess the number in between 1 to 10" << endl;
            cin >> GuessNumber;

            // Randomly generated number
            RandomNumber = rand() % 10 + 1;  // rand() % (max - min +1) + 1

            // if correct guess
            if(RandomNumber == GuessNumber){
                cout << "Random Number Generated is " << RandomNumber << endl;
                cout << "Congrats! You Got it Right" << endl << endl;

                amount = (amount - betAmount) + betAmount*5;
                cout << "Your Current Total Balance is: " << amount;
                cout << endl;
            }

            // if wrong guess
            else if(RandomNumber != GuessNumber){
                cout << "Random Number Generated is " << RandomNumber << endl;
                cout << "Sorry, you failed this time." << endl << endl;
                amount = amount - betAmount;
                cout << "Your Current Total Balance is: " << amount;
                cout << endl;
            }

            // if balance is going down of 1000
            if(amount < 1000){
                cout << "You Will eliminated from the game due to insufficient balance." << endl;

                char yes_no;
                cout << "Do you want to continue(y/n): ";   
                cin >> yes_no;
                switch (yes_no)
                {
                case 'y':
                    setAmount();
                    continue;
                
                case 'n': exit_from_game();
                    break;
                }

            }
            
            char yes_no;
            cout << "Will you continue (y/n): ";
            cin >> yes_no;

            switch (yes_no)
            {
            case 'y': break;
            case 'n': exit_from_game();
                break;

            }

        }
    }
    
    void TheGame(){
        setName();
        setAmount();
        GameLoop();
    }
};

int main(){
    cout << "-------------------------------------------------------" << endl;
    cout << "**********  Welcome To The Game  **********" << endl;
    cout << "-------------------------------------------------------" << endl << endl;

    Casino game;
    game.showRules();
    cout << endl;

    game.TheGame();

}
