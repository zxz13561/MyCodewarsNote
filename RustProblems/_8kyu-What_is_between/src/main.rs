/// Complete the function that takes two integers (a, b, where a < b)
/// and return an array of all integers between the input parameters,
/// including them.
/// a = 1
/// b = 4
// --> [1, 2, 3, 4]

fn main() {
    let v = between(1, 4);
    println!("{:?}", v);
}

fn between(a: i16, b: i16) -> Vec<i16> {
    (a..=b).collect()
}
