fn main() {
    test_basics();
}

fn test_basics() {
    assert_eq!(derive(7, 8), "56x^7");
    assert_eq!(derive(5, 9), "45x^8");
}

fn derive(coefficient: u32, exponent: u32) -> String {
    [(coefficient * exponent).to_string(), (exponent-1).to_string()].join("x^")
}

fn better(coefficient: u32, exponent: u32) -> String {
    format!("{}x^{}", coefficient * exponent, exponent - 1)
}
