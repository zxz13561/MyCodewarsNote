fn main() {
    test_basic();
}

fn test_basic() {
    assert_eq!(name_shuffler("john McClane"), "McClane john");
    assert_eq!(name_shuffler("Mary jeggins"), "jeggins Mary");
    assert_eq!(name_shuffler("tom jerry"), "jerry tom");
}

fn name_shuffler(s: &str) -> String {
    let _split: Vec<_> = s.split(' ').rev().collect();
    _split.join(" ")
}

fn best_solution(s: &str) -> String{
    s.rsplit(" ").collect::<Vec<&str>>().join(" ")
}