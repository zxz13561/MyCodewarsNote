fn sample_tests() {
    dotest(&[], &[]);
    dotest(&["a", "b", "c"], &["1: a", "2: b", "3: c"]);
    dotest(&["", "", ""], &["1: ", "2: ", "3: "]);
    dotest(&["", "b", "", ""], &["1: ", "2: b", "3: ", "4: "]);
}
fn dotest(arr: &[&str], expected: &[&str]) {
    let actual = number(arr);
    assert_eq!(actual, expected, "With lines= {arr:?}\nExpected {expected:?}\nBut got {actual:?}")
}

fn number(lines: &[&str]) -> Vec<String> {
    // The best
    // lines.iter().enumerate().map(|x| format!("{}: {}", x.0 + 1, x.1)).collect()

    let mut vec = Vec::new();
    for (idx, _s) in lines.iter().enumerate() {
        let _tmp_str = (idx+1).to_string() + ": " + _s;
        vec.push(_tmp_str);
    }
    vec
}

fn main() {
    sample_tests();
}
