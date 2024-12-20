use std::collections::HashMap;

fn main() {
    sample();
}

fn sample() {
    do_test(&[1, 2, 3], 4);
    do_test(&[1234, 5678, 9012], 14690);
    do_test(&[2, 2, 3], 4);
    do_test(&[1, 1, 2, 2, 3, 3, 4], 6);
}

fn do_test(nums: &[i32], sum: i32) {
    let len = nums.len();
    let user_tuple = two_sum(nums, sum);
    assert!(
        user_tuple.0 < len && user_tuple.1 < len,
        "\nnumbers: {:?}\ntarget: {}\nresult: {:?}\nresult tuple has an index out of bounds",
        nums, sum, user_tuple
    );
    assert!(
        user_tuple.0 != user_tuple.1,
        "\nnumbers: {:?}\ntarget: {}\nresult: {:?}\nresult tuple must have two different indices",
        nums, sum, user_tuple
    );
    let num1 = nums[user_tuple.0];
    let num2 = nums[user_tuple.1];
    let user_sum = num1 + num2;
    assert!(
        user_sum == sum,
        "\nnumbers: {:?}\ntarget: {}\nresult: {:?}\nnumber as index {}: {}\nnumber as index {}: {}\nsum of the two numbers: {}\nsum of the two numbers did not equal target",
        nums, sum, user_tuple, user_tuple.0, num1, user_tuple.1, num2, user_sum
    )
}

// fn two_sum(numbers: &[i32], target: i32) -> (usize, usize) {
//     let mut _res = (0, 0);
//     for (i, n1) in numbers.iter().enumerate() {
//         _res.0 = i;
//         for (j, n2) in numbers[i+1..].iter().enumerate() {
//             _res.1 = i+j+1;
//             if n1 + n2 == target {
//                 return _res
//             }
//         }
//     }
//     _res
// }

fn two_sum(numbers: &[i32], target: i32) -> (usize, usize) {
    let mut map = HashMap::with_capacity(numbers.len());
    println!("{:?}", map);
    for (i, &v) in numbers.iter().enumerate() {
        match map.get(&(target - v)) {
            Some(&idx) => return (i, idx),
            None => map.insert(v, i),
        };
        println!("{:?}", map);
    }
    unreachable!();
}
