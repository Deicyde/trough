---
declaration: theorem
origin: cited
lean: OeisA103662.conjecture, OeisA103662.conjecture.variants.a_40
statement: formalized
---

# Smallest power with base>1 and exponent $n$ without digit 0

> For statistical reasons it is conjectured that the sequence is finite.
> Also it is conjectured that $a(40)$ does not exist (i.e. the sequence is empty for $n=40$).
>
> *References:*
> - [A103662](https://oeis.org/A103662)

*Quoted from [FormalConjectures/OEIS/103662.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103662.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 4 test statements, counted here but not shown.

## `OeisA103662.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA103662_conjecture.lean#L191](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA103662_conjecture.lean#L191).

> For statistical reasons it is conjectured that the sequence is finite.
> Finite means here that for some $n$, no power $b^n$ with base $b > 1$ has a zeroless decimal
> representation, which in our definition results in $a(n) = 0$.
>
> This holds for $n = 2500$
> ([source](https://tadamcz.com/fc-review-results/aea251bb26/#/f/OEIS/103662)).
> Take any integer $b > 1$ and let $N = b^{2500}$. Since $b \ge 2$, we have
> $N \ge 2^{2500} > 10^5$, so $N$ has at least six decimal digits. We split into four cases
> depending on the divisibility of $b$ by $2$ and $5$:
>
> - **If $10 \mid b$:** Then $10 \mid N$, so the units digit of $N$ is $0$.
> - **If $b$ is odd and $5 \nmid b$:** Since $b$ is odd and the Carmichael function satisfies
>   $\lambda(16) = 4 \mid 2500$, we have $N \equiv 1 \pmod{16}$. Since $5 \nmid b$ and
>   $\varphi(5^5) = 2500$, Euler's totient theorem gives $N \equiv 1 \pmod{3125}$. By the Chinese
>   Remainder Theorem, $N \equiv 1 \pmod{50000}$ (as $16 \cdot 3125 = 50000$), so the tens digit
>   of $N$ is $0$.
> - **If $b$ is odd and $5 \mid b$:** As above, $N \equiv 1 \pmod{16}$. Since $5 \mid b$ and
>   $2500 \ge 4$, we also have $5^4 = 625 \mid N$, so $N \equiv 0 \pmod{625}$. Since
>   $16 \cdot 625 = 10^4$ and $625 \equiv 1 \pmod{16}$, the Chinese Remainder Theorem gives
>   $N \equiv 625 \pmod{10^4}$. Because $N > 10^4$, the last four digits of $N$ are $0625$, so its
>   thousands digit is $0$.
> - **If $b$ is even and $5 \nmid b$:** Since $2 \mid b$ and $2500 \ge 5$, we have
>   $2^5 = 32 \mid N$, so $N \equiv 0 \pmod{32}$. Since $5 \nmid b$, Euler's theorem again gives
>   $N \equiv 1 \pmod{3125}$. Because $32 \cdot 3125 = 10^5$ and
>   $9376 = 293 \cdot 32 = 3 \cdot 3125 + 1$, the Chinese Remainder Theorem gives
>   $N \equiv 9376 \pmod{10^5}$. Since $N > 10^5$, the last five digits of $N$ are $09376$, so its
>   ten-thousands digit is $0$.
>
> In every case, the decimal representation of $N$ contains the digit $0$, so $a(2500) = 0$.

```lean
theorem conjecture : ∃ n : ℕ, a n = 0
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/103662.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103662.lean#L114).

## `OeisA103662.conjecture.variants.a_40`

Open: stated without proof.

> $a(40)$, if it exists, is not known.
>
> This claim is rooted in the finiteness conjecture. The most direct mathematical expression
> of the open problem concerning $a(40)$ is the negation of the existence of a valid base.

```lean
theorem conjecture.variants.a_40 :
  ¬ ∃ (b : ℕ), IsValidZerolessPower 40 b
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/103662.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103662.lean#L124).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/103662.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103662.lean)
- [A103662](https://oeis.org/A103662)
