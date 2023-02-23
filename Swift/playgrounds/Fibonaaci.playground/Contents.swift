import UIKit

func fibbonacci(indexed: Int) -> Any {
    let indexed = indexed + 1
    var sequenceOfNums = [Int]()
    
    for i in 0...indexed {
        if i <= 1 {
            sequenceOfNums.append(i)
        }
        else {
            let num : Int = sequenceOfNums[i-2] + sequenceOfNums[i-1]
            sequenceOfNums.append(num)
        }
    }
    
    return sequenceOfNums
}

print(fibbonacci(indexed: 50))
