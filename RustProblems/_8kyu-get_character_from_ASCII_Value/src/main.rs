fn main() {
    example();
}

fn example() {
    assert_eq!(get_char(55), '7');
    assert_eq!(get_char(56), '8');
    assert_eq!(get_char(57), '9');
    assert_eq!(get_char(58), ':');
    assert_eq!(get_char(59), ';');
    assert_eq!(get_char(60), '<');
    assert_eq!(get_char(61), '=');
    assert_eq!(get_char(62), '>');
    assert_eq!(get_char(63), '?');
    assert_eq!(get_char(64), '@');
    assert_eq!(get_char(65), 'A');
}

fn get_char(c: i32) -> char {
    char::from_u32(c as u32).unwrap()
}

fn get_char_best(c: i32) -> char {
    c as u8 as char
}

