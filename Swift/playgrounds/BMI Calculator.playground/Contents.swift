func bmiCalculator(mass: Float, height: Float) -> String {
    let bmi : Float = mass/(height * height)
    
    if bmi > 25 {
        return "You are overweight"
    }
    else if bmi >= 18.5 && bmi <= 25 {
        return "You are normal weight"
    }
    else {
        return "You are underweight"
    }
}

print(bmiCalculator(mass: 50, height: 50))
