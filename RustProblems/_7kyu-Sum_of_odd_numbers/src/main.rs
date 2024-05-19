fn main() {
    let arr = [1, 2, 3, 4, 5, 6, 7, 8, 10];
    let _res = first_non_consecutive(&arr);
    println!("{:?}", _res);
}

fn first_non_consecutive(arr: &[i32]) -> Option<i32> {
    println!("{:?}", arr.windows(2));
    println!("{:?}", arr.windows(2).find(|s| s[0] + 1 != s[1]));
    println!("{:?}", arr.windows(2).map(|s| s[1]));
    arr.windows(2).find(|s| s[0] + 1 != s[1]).map(|s| s[1])
}