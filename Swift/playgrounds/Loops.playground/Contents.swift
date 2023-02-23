import UIKit

let arrayOfNumbers = [1, 5, 3, 6, 2, 7, 23, 34, 32, 21, 12]

//var sum = 0
//
//for number in arrayOfNumbers {
//    sum += number
//}
//
//print(sum)

/* printing ranges */
//for number in 1...10 {
//    print(number)
//}

//for number in 1..<10 {
//    print(number)
//}

//for number in 1..<10 where number % 2 == 0 {
//    print(number)
//}

/* 99 bottles of beer */

//func beerSong(withThisManyBottles totalNumberOfBottles : Int) -> String {  // first var is outside param and the second one is the inside param
func beerSong(_ totalNumberOfBottles : Int) -> String {  // first var is outside param and the second one is the inside param
    var lyrics: String = ""
    
    for number in (1...totalNumberOfBottles).reversed() {
        var newLine : String = ""

        if number > 1 {
            newLine = "\n\(number) bottles of beer on the wall, \(number) bottles of beer. \nTake one down and pass it around, \(number - 1) bottles of beer on the wall.\n"
        }
        else {
            newLine = "\n\(number) bottle of beer on the wall, \(number) bottle of beer. \nTake one down and pass it around, no more bottles of beer on the wall.\n"
        }
        
        lyrics += newLine
    }
    
    lyrics += "\nNo more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, \(totalNumberOfBottles) bottles of beer on the wall.\n"
    
    return lyrics
}

print(beerSong(25))  // when underscore is used, there is no need for outside param


