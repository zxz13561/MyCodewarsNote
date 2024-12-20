fn main() {
    let res = other(7);
    if let Some(ret) = res {
        println!("{}", ret);
    } else {
        println!("Error value!!");
    }
}

fn print(n: i32) -> Option<String> {
    if n <= 0 || n % 2 == 0{
        return None;
    }
    else if n == 1 {
        return Some("*\n".to_string());
    }

    let mut s = String::new();
    let mut top_v = n;
    let mut blank = n / 2;
    let mut star = 1;

    while star < n {
        for _ in 0..blank {
            s.push(' ');
        }
        blank = blank - 1;
        for _ in 0..star {
            s.push('*');
        }
        star += 2;

        s.push('\n');
    }

    blank = 0;
    while top_v > 0 {
        for _ in 0..blank {
            s.push(' ');
        }
        for _ in 0..top_v {
            s.push('*');
        }
        s.push('\n');
        top_v = top_v - 2;
        blank += 1;
    }

    Some(s)
}

fn other(n: i32) -> Option<String> {
    if n < 0 || n % 2 == 0 {
        return None;
    }

    let n = n as usize;
    let diamond = (1..=n)
        .chain((1..n).rev())
        .step_by(2)
        .map(|i| format!("{}{}\n", " ".repeat((n - i) / 2), "*".repeat(i)))
        .collect();

    Some(diamond)
}
