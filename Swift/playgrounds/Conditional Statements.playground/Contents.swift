import UIKit

func loveCalculator (yourname : String, theirName : String) -> String {
    let loveScore = arc4random_uniform(101)
    
    // && is and,|| is or, != is not
    if loveScore > 80 {
        return "Your love score is \(loveScore), You love each other."
    }
    else if loveScore > 40 && loveScore <= 80 {
        return "Your love score is \(loveScore), You go together like coke and mentos"
    }
    else {
        return "Your love score is \(loveScore), No love possible."
    }
    
}

print(loveCalculator(yourname: "Ike", theirName: "Jill Doe"))
