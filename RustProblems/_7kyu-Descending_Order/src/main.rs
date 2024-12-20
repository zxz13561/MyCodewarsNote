fn main() {
    returns_expected();
}

fn returns_expected() {
    assert_eq!(descending_order(0), 0);
    assert_eq!(descending_order(1), 1);
    assert_eq!(descending_order(15), 51);
    assert_eq!(descending_order(1021), 2110);
    assert_eq!(descending_order(123456789), 987654321);
    assert_eq!(descending_order(145263), 654321);
    assert_eq!(descending_order(1254859723), 9875543221);
}

fn descending_order(x: u64) -> u64 {
    let mut _num:Vec<char> = x.to_string().chars().collect();
    _num.sort();
    _num.reverse();
    _num.iter().collect::<String>().parse().unwrap()
}