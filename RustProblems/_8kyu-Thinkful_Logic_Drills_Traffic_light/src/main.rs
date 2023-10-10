fn main() {
    basic_test();
}

fn basic_test() {
    assert_eq!(update_light("green"), "yellow");
    assert_eq!(update_light("yellow"), "red");
    assert_eq!(update_light("red"), "green");
}

fn update_light(current: &str) -> String {
    match current {
        "green" => format!("yellow"),
        "yellow" => format!("red"),
        "red" => format!("green"),
        _=> panic!()
    }
}
