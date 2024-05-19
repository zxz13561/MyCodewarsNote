fn main() {
    sample_test();
}

fn sample_test() {
    assert!(is_valid_ip("0.0.0.0"));
    assert!(is_valid_ip("12.255.56.1"));
    assert!(is_valid_ip("137.255.156.100"));

    assert!(!is_valid_ip(""));
    assert!(!is_valid_ip("abc.def.ghi.jkl"));
    assert!(!is_valid_ip("123.456.789.0"));
    assert!(!is_valid_ip("12.34.56"));
    assert!(!is_valid_ip("01.02.03.04"));
    assert!(!is_valid_ip("256.1.2.3"));
    assert!(!is_valid_ip("1.2.3.4.5"));
    assert!(!is_valid_ip("123,45,67,89"));
    assert!(!is_valid_ip("1e0.1e1.1e2.2e2"));
    assert!(!is_valid_ip(" 1.2.3.4"));
    assert!(!is_valid_ip("1.2.3.4 "));
    assert!(!is_valid_ip("12.34.56.-7"));
    assert!(!is_valid_ip("1.2.3.4\n"));
    assert!(!is_valid_ip("\n1.2.3.4"));
}

fn is_valid_ip(ip: &str) -> bool {
    let _split:Vec<&str> = ip.split('.').collect();

    if _split.len() != 4 {
        return false;
    }

    for v in _split.into_iter() {
        if v.len() > 1 && v.chars().next().unwrap() == '0' {
            return false;
        }
        match v.parse::<i32>() {
            Ok(_n) => {if _n > 255 || _n < 0 { return false; }},
            Err(_) => return false
        }
    }
    return true
}

/*
use std::net::Ipv4Addr;
fn is_valid_ip(ip: &str) -> bool {
    ip.parse::<Ipv4Addr>().is_ok()
}
*/