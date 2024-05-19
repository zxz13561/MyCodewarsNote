fn main() {
    returns_expected();
}

fn returns_expected() {
    assert_eq!(good_vs_evil("0 0 0 0 0 10", "0 0 0 0 0 0 0"), "Battle Result: Good triumphs over Evil");
    assert_eq!(good_vs_evil("0 0 0 0 0 0", "0 0 0 0 0 0 10"), "Battle Result: Evil eradicates all trace of Good");
    assert_eq!(good_vs_evil("0 0 0 0 0 10", "0 0 0 0 0 0 10"), "Battle Result: No victor on this battle field");
}

fn good_vs_evil(good: &str, evil: &str) -> String {
    let _g_worth = vec![1, 2, 3, 3, 4, 10];
    let _e_worth = vec![1, 2, 2, 2, 3, 5, 10];

    let _vg:i32 = good
        .split(' ')
        .zip(_g_worth.iter())
        .map(|(s, w)| s.parse::<i32>().unwrap() * w)
        .sum();

    let _ve:i32 = evil
        .split(' ')
        .zip(_e_worth.iter())
        .map(|(s, w)| s.parse::<i32>().unwrap() * w)
        .sum();

    match _vg - _ve {
        x if x > 0 => { "Battle Result: Good triumphs over Evil".to_string() },
        x if x < 0 => { "Battle Result: Evil eradicates all trace of Good".to_string() },
        x if x == 0 => { "Battle Result: No victor on this battle field".to_string() }
        _ => "ERROR OCCURRED!".to_string()
    }
}