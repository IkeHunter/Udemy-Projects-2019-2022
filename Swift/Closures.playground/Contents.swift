import UIKit

//func calculator (n1: Int, n2: Int, operation: (Int, Int) -> Int) -> Int {  // data type is in the form of a boiled down version of a function
//    return operation(n1, n2)
//}
//
////func add (no1: Int, no2: Int) -> Int {
////    return no1 + no2
////}
//
//
//// $0 means first var, $1 means second
//let result = calculator(n1: 2, n2: 3) { $0 * $1 }
//
//print(result)
//---
//let array = [6, 2, 3, 9, 4, 1]
//
//
//
//let newArray = array.map{"\($0)"}
//
//print(newArray)
//---

class Firebase {
    func createUser (username: String, password: String, completion: (Bool, Int) -> Void) {  // void because there is no return
        
        //does something time consuming
        var isSuccess = true
        var userID = 123
        
        completion(isSuccess, userID)
        
    }
}

class MyApp {
    func registerButtonPressed () {
        
        let firebase = Firebase()
        
        firebase.createUser(username: "John Doe", password: "123456") {
            (isSuccess, userID) in
            print("registration is successful: \(isSuccess)")
            print("userID is: \(userID)")
        }
    }
    
    
}

let myApp = MyApp()
myApp.registerButtonPressed()


