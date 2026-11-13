---
declaration: theorem
origin: cited
lean: Green59.green_59, Green59.green_59.variants.balog
statement: formalized
---

# Ben Green's Open Problem 59

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.59)
> - [Er82] Erdős, P., *Some new problems and results in number theory*. Number theory (Mysore,
>   1981), Lecture Notes in Math. 938, Springer (1982), 50--74.
> - [Ba89] Balog, A., *On additive representation of integers*. Acta Math. Hungar. 54 (1989),
>   297--301.
> - [NS08] Naccache, D. and Shparlinski, I. E., *Divisibility, smoothness and cryptographic
>   applications*. [arXiv:0810.2067](https://arxiv.org/abs/0810.2067) (2008).
> - [DVA21] Dimitrov, V., Vigneri, L. and Attias, V., *Fast generation of RSA keys using smooth
>   integers*. IEEE Trans. Comput. (2021).
>   [arXiv:1912.11546](https://arxiv.org/abs/1912.11546)

*Quoted from [FormalConjectures/GreensOpenProblems/59.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/59.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement, counted here but not shown.

## `Green59.green_59`

Open: stated without proof.

> Is every $n \le N$ the sum of two integers, all of whose prime factors are at most
> $N^\varepsilon$?
>
> We read this as: for every $\varepsilon > 0$ and every sufficiently large $N$, every integer
> $2 \le n \le N$ is $a + b$ with positive integers $a, b$ whose prime factors are all at most
> $N^\varepsilon$. Positive summands exclude $n = 1$. [Gr24] quotes Erdős [Er82] for an
> essentially equivalent conjecture, which is
> [Erdős Problem 334](https://www.erdosproblems.com/334). [Gr24] also reports a remark of Wooley:
> a positive answer for every $\varepsilon > 0$ would solve Vinogradov's least quadratic
> non-residue problem for primes $p \equiv 3 \pmod 4$.

```lean
theorem green_59 :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ N : ℕ in atTop, ∀ n ∈ Finset.Icc 2 N, ∃ a b : ℕ, 0 < a ∧ 0 < b ∧
      a + b = n ∧ IsSmooth ((N : ℝ) ^ ε) a ∧ IsSmooth ((N : ℝ) ^ ε) b
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/59.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/59.lean#L69).

## `Green59.green_59.variants.balog`

Solved: stated here without proof.

> **Balog's theorem.** For every $\varepsilon > 0$, every sufficiently large integer $N$ is
> $n_1 + n_2$ with positive integers $n_1, n_2$ whose prime factors are all at most
> $N^{4/(9\sqrt{e}) + \varepsilon}$, where $4/(9\sqrt{e}) \approx 0.2695$.
>
> This is due to Balog [Ba89]. We take it from [NS08, Section 6.6], which states it with exponent
> $4/(9\sqrt{e})$, and [DVA21, Theorem 4], which states it with exponent
> $4/(9\sqrt{e}) + \varepsilon$, as here. Applied to each large $n \le N$ (and with
> $n = 1 + (n - 1)$ for small $n$), it gives `green_59` with $\varepsilon$ replaced by any number
> greater than $4/(9\sqrt{e})$; [Gr24] says this is still the record.

```lean
theorem green_59.variants.balog :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ N : ℕ in atTop, ∃ a b : ℕ, 0 < a ∧ 0 < b ∧ a + b = N ∧
      IsSmooth ((N : ℝ) ^ (4 / (9 * Real.sqrt (Real.exp 1)) + ε)) a ∧
      IsSmooth ((N : ℝ) ^ (4 / (9 * Real.sqrt (Real.exp 1)) + ε)) b
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/59.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/59.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/59.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/59.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.59)
