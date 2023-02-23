//
//  Car.swift
//  Classes and Objects
//
//  Created by Isaac Hunter on 9/5/19.
//  Copyright © 2019 Isaac Hunter. All rights reserved.
//

import Foundation

enum CarType {
    case Sedan
    case Coupe
    case Hatchback
}

class Car {
    
    var color = "Black"
    var numberOfSeats = 5
    var typeOfCar : CarType = .Coupe
    
//    init(customerChosenColor : String, numberOfSeats : Int) {  // compusrary perameter
//        color = customerChosenColor
//    }
    
    init() {  // compusrary perameter
        
    }
    
    convenience init (customerChosenColor : String) {
        self.init()
        color = customerChosenColor
    }
    
    func drive() {
        print("car is moving")
    }
}
