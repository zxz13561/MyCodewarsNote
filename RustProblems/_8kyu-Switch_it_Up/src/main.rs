fn main() {
    basic();
}

fn basic() {
    assert_eq!(switch_it_up(1), "One");
    assert_eq!(switch_it_up(2), "Two");
    assert_eq!(switch_it_up(3), "Three");
}

fn switch_it_up(n: usize) -> &'static str {
    match n {
        1=>"One",
        2=>"Two",
        3=>"Three",
        4=>"Four",
        5=>"Five",
        6=>"Six",
        7=>"Seven",
        8=>"Eight",
        9=>"Nine",
        0=>"Zero",
        _=> panic!()
    }
}