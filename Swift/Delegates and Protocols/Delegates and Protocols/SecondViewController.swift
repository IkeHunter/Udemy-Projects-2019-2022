//
//  SecondViewController.swift
//  Delegates and Protocols
//
//  Created by Isaac Hunter on 9/27/19.
//  Copyright © 2019 Isaac Hunter. All rights reserved.
//

import UIKit

protocol CanReceive {
    
    func dataReceived(data: String)
    
}

class SecondViewController: UIViewController {
    
    var delegate : CanReceive?
    
    var data = ""
    
    @IBOutlet weak var label: UILabel!
    
    @IBOutlet weak var textField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        label.text = data

    }
    
    
    @IBAction func sendDataBack(_ sender: Any) {
        
        delegate?.dataReceived(data: textField.text!)
        dismiss(animated: true, completion: nil)
        
    }
    
   
}
