---
declaration: theorem
origin: cited
lean: OeisA51903.conjecture1, OeisA51903.conjecture2, OeisA51903.conjecture3
statement: formalized
---

# Maximum exponent in the prime factorization of $n$

> *References:*
> - [A051903](https://oeis.org/A051903)

*Quoted from [FormalConjectures/OEIS/51903.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/51903.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 5 test statements, counted here but not shown.

## `OeisA51903.conjecture1`

Open: stated without proof.

> Are there composite numbers $n > 4$ such that $n \equiv a(n) \pmod{\phi(n)}$?
> - Thomas Ordowski, Dec 02 2019
>
> This question is equivalent to Lehmer's totient problem `LehmerTotient.lehmer_totient`; a
> positive answer here falsifies the universal statement asked about in
> `Erdos828.erdos_828.variants.lehmer_conjecture`. Any composite
> $n$ with $\phi(n) \mid n - 1$ is squarefree, so $a(n) = 1$ and the condition here holds.
> Conversely, let $n > 4$ be composite with $\phi(n) \mid n - a(n)$ and $e = a(n) \ge 2$, and
> pick $p$ with $p^e \mid n$. Then $p^{e-1} \mid \phi(n) \mid n - e$ and $p^{e-1} \mid n$, so
> $p^{e-1} \mid e$, which forces $p = 2$ and $e = 2$. Now $n = 4m$ with $m$ odd and squarefree,
> and $2\phi(m) \mid 4m - 2$ makes $\phi(m)$ odd, so $m = 1$ and $n = 4$. Hence $e = 1$ and the
> condition is $\phi(n) \mid n - 1$.

```lean
theorem conjecture1 :
    ∃ n : ℕ, 4 < n ∧ ¬ n.Prime ∧ n.totient ∣ (n - a n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/51903.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/51903.lean#L69).

## `OeisA51903.conjecture2`

Solved: stated here; a Lean proof is at [https://github.com/anshM123/OEIS-A051903/blob/c0104e7a9cc2d76d86c3a277c372f91a9553a0f6/lean/DMSolutions/OEIS_A051903/Solution.lean#L21-L24](https://github.com/anshM123/OEIS-A051903/blob/c0104e7a9cc2d76d86c3a277c372f91a9553a0f6/lean/DMSolutions/OEIS_A051903/Solution.lean#L21-L24).

> Are there odd numbers $n$ such that $a(n) > 1$ and $n \equiv a(n) \pmod{\lambda(n)}$?
> (Equivalently, odd numbers $n$ such that $a(n) > 1$ and $b^n \equiv b^{a(n)} \pmod n$ for all $b$.)
> - Thomas Ordowski, Dec 02 2019
>
> The answer is no. Let $q^E \| n$ with $E = a(n) \ge 2$ and take $b = q + 1$: then
> $(q+1)^{n-E} \equiv 1 \pmod{q^E}$, so lifting the exponent gives $q^{E-1} \mid n - E$. Since also
> $q^{E-1} \mid n$, we get $q^{E-1} \mid E$, which is impossible for $q \ge 3$.

```lean
theorem conjecture2 :
    ¬ ∃ n : ℕ, Odd n ∧ 1 < a n ∧ ∀ b : ℕ, b ^ n ≡ b ^ (a n) [MOD n]
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/51903.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/51903.lean#L85).

## `OeisA51903.conjecture3`

Solved: stated here; a Lean proof is at [https://github.com/anshM123/OEIS-A051903/blob/c0104e7a9cc2d76d86c3a277c372f91a9553a0f6/lean/DMSolutions/OEIS_A051903/Solution.lean#L27-L30](https://github.com/anshM123/OEIS-A051903/blob/c0104e7a9cc2d76d86c3a277c372f91a9553a0f6/lean/DMSolutions/OEIS_A051903/Solution.lean#L27-L30).

> Are there odd numbers $n$ such that $a(n) > 1$ and $n \equiv a(n) \pmod{\operatorname{ord}_n(2)}$?
> (Equivalently, odd numbers $n$ such that $a(n) > 1$ and $2^n \equiv 2^{a(n)} \pmod n$.)
> - Thomas Ordowski, Dec 02 2019
>
> The answer is yes: $n = 7 \cdot 631 \cdot 881 \cdot 3511^2 \cdot 201961 = 9687963167864344937$ is odd,
> $a(n) = 2$ and $2^n \equiv 2^2 \pmod n$. A square factor $q^2 \mid n$ forces $q$ to be a Wieferich
> prime; $3511$ works because $\operatorname{ord}_{3511^2}(2) = 1755$ is odd and $n \equiv 2 \pmod{1755}$.

```lean
theorem conjecture3 :
    ∃ n : ℕ, Odd n ∧ 1 < a n ∧ 2 ^ n ≡ 2 ^ (a n) [MOD n]
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/51903.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/51903.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/51903.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/51903.lean)
- [A051903](https://oeis.org/A051903)
