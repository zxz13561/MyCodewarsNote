/// Given an array of integers.
///
/// Return an array, where the first element is the count of positives
/// numbers and the second element is sum of negative numbers. 0 is
/// neither positive nor negative.
///
/// If the input is an empty array or is null, return an empty array.

fn main() {
    dotest(&[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], &[10, -65]);
    dotest(&[], &[]);
    dotest(&[0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14], &[8, -50]);
    dotest(&[0,1,2,3,4,5], &[5, 0]);
    dotest(&[1,2,3,4,5], &[5, 0]);
    dotest(&[0,-1,-2,-3,-4,-5], &[0, -15]);
    dotest(&[-1,-2,-3,-4,-5], &[0, -15]);
    dotest(&[0,0,0,0], &[0,0]);
    dotest(&[0], &[0,0]);
}

fn dotest(a: &[i32], expected: &[i32]) {
    let actual = count_positives_sum_negatives(a.to_vec());
    assert!(actual == expected,
            "With input = {a:?}\nExpected {expected:?} but got {actual:?}")
}

fn count_positives_sum_negatives(input: Vec<i32>) -> Vec<i32> {
    if input.is_empty() {
        return vec![];
    }

    input.iter().fold(vec![0, 0], |mut acc, &x| {
        if x > 0 {
            acc[0] += 1;
        } else {
            acc[1] += x;
        }
        acc
    })
}

fn filter(input: Vec<i32>) -> Vec<i32> {
    if input.is_empty() {
        return Vec::new();
    }

    vec![
        input.iter().filter(|&&x| x > 0).count() as i32,
        input.iter().filter(|&&x| x < 0).sum()
    ]
}

fn first_try(input: Vec<i32>) -> Vec<i32> {
    if input.is_empty() {
        return Vec::new();
    }
    let mut neg = 0;
    let mut pos = 0;

    for v in input {
        if v >= 1 {
            pos += 1;
        } else {
            neg += v;
        }
    }

    vec![pos, neg]
}


