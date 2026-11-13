---
declaration: theorem
origin: cited
lean: PfisterPythagorasNumber.pfister_problem, PfisterPythagorasNumber.pfister_problem.variants.eq_two_pow, PfisterPythagorasNumber.pfister_problem.variants.upper_bound, PfisterPythagorasNumber.pfister_problem.variants.cassels, PfisterPythagorasNumber.pfister_problem.variants.add_one_le, PfisterPythagorasNumber.pfister_problem.variants.lower_bound, PfisterPythagorasNumber.pfister_problem.variants.zero, PfisterPythagorasNumber.pfister_problem.variants.one, PfisterPythagorasNumber.pfister_problem.variants.two
statement: formalized
---

# Pfister's problem on the Pythagoras number of $\mathbb{R}(X_1, \dots, X_n)$

> The Pythagoras number $p(K)$ of a field $K$ is the least $p$ such that every sum of squares in
> $K$ is a sum of $p$ squares, i.e. the least element of `pythagorasBounds K`.
>
> Artin's solution of Hilbert's 17th problem shows that a positive semidefinite rational function
> in $\mathbb{R}(X_1, \dots, X_n)$ is a sum of squares, and Pfister showed that $2^n$ squares
> suffice ([Pfister1967, Theorem 1]; for the field, Corollary 1 of Theorem 2 in [Pfister1971]).
> Since sums of squares are positive semidefinite, $p(\mathbb{R}(X_1, \dots, X_n)) \le 2^n$
> [Pfister1995, p. 95].
>
> Problem 1 of [Pfister1971, §4] asks for the true value of $p(\mathbb{R}(X_1, \dots, X_n))$.
> The question is often posed as: is $p(\mathbb{R}(X_1, \dots, X_n)) = 2^n$, i.e. is Pfister's
> bound optimal? See e.g. [Benoist2017, Question 0.2].
>
> Problem 1 itself quotes the lower bound $n + 1 \le p(\mathbb{R}(X_1, \dots, X_n))$ from Cassels'
> theorem [Cassels1964]. For $n \ge 2$ the best known bounds are
> $n + 2 \le p(\mathbb{R}(X_1, \dots, X_n)) \le 2^n$ [Pfister1995, p. 97], where the lower bound
> follows from the Cassels–Ellison–Pfister theorem [CEP1971]. The bounds agree for $n = 2$, so the
> value is known for $n \le 2$ and open for every $n \ge 3$. The survey
> [MerkurjevParimala2025, §5.2] records the question as open even for $\mathbb{R}(X_1, X_2, X_3)$
> (Question 5.7).
>
> *References:*
> - [Pfister1971] A. Pfister, *Sums of squares in real function fields*, pp. 297–300 in Actes du
>   Congrès International des Mathématiciens, Tome 1 (Nice, 1970), Gauthier-Villars, 1971,
>   [IMU scan](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1970.1/ICM1970.1.ocr.pdf).
> - [Pfister1967] A. Pfister, *Zur Darstellung definiter Funktionen als Summe von Quadraten*,
>   Invent. Math. 4 (1967), 229–237, [doi:10.1007/BF01425382](https://doi.org/10.1007/BF01425382).
> - [Cassels1964] J. W. S. Cassels, *On the representation of rational functions as sums of squares*,
>   Acta Arith. 9 (1964), 79–82, [doi:10.4064/aa-9-1-79-82](https://doi.org/10.4064/aa-9-1-79-82).
> - [Pfister1995] A. Pfister, *Quadratic forms with applications to algebraic geometry and
>   topology*, London Math. Soc. Lecture Note Ser. 217, Cambridge University Press, 1995.
> - [CEP1971] J. W. S. Cassels, W. J. Ellison, A. Pfister, *On sums of squares and on elliptic
>   curves over function fields*, J. Number Theory 3 (1971), 125–149,
>   [doi:10.1016/0022-314X(71)90030-8](https://doi.org/10.1016/0022-314X(71)90030-8).
> - [Benoist2017] O. Benoist, *On Hilbert's 17th problem in low degree*, Algebra Number Theory 11
>   (2017), 929–959, [doi:10.2140/ant.2017.11.929](https://doi.org/10.2140/ant.2017.11.929),
>   [arXiv:1602.07330](https://arxiv.org/abs/1602.07330).
> - [MerkurjevParimala2025] A. Merkurjev, R. Parimala, *Quadratic forms beyond arithmetic*, Notices
>   Amer. Math. Soc. 72 (2025), no. 7, 711–718,
>   [doi:10.1090/noti3192](https://doi.org/10.1090/noti3192).

*Quoted from [FormalConjectures/Paper/PfisterPythagorasNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PfisterPythagorasNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 9 research or textbook statements: 2 open, 5 solved and 2 textbook results. It also has 1 test statement, counted here but not shown.

## `PfisterPythagorasNumber.pfister_problem`

Open: stated without proof.

> **Pfister's problem** (Problem 1 of [Pfister1971, §4]): what is the true value of
> $p(\mathbb{R}(X_1, \dots, X_n))$, as a function of $n$? It is $1$, $2$, $4$ for $n = 0, 1, 2$
> (`pfister_problem.variants.zero`, `pfister_problem.variants.one`, `pfister_problem.variants.two`)
> and open for every $n \ge 3$, where only the bounds
> $n + 2 \le p(\mathbb{R}(X_1, \dots, X_n)) \le 2^n$ are known.

```lean
theorem pfister_problem :
    ∀ n, IsLeast (pythagorasBounds (MvRatFunc (Fin n) ℝ)) (pfister_problem.answer n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/PfisterPythagorasNumber.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PfisterPythagorasNumber.lean#L90).

## `PfisterPythagorasNumber.pfister_problem.variants.eq_two_pow`

Open: stated without proof.

> Pfister's problem in its common yes/no form (e.g. Question 0.2 of [Benoist2017]): is
> $p(\mathbb{R}(X_1, \dots, X_n)) = 2^n$ for every $n$, i.e. is Pfister's bound optimal? This
> holds for $n \le 2$ and is open for every $n \ge 3$.

```lean
theorem pfister_problem.variants.eq_two_pow :
    ∀ n : ℕ, IsLeast (pythagorasBounds (MvRatFunc (Fin n) ℝ)) (2 ^ n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/PfisterPythagorasNumber.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PfisterPythagorasNumber.lean#L100).

## `PfisterPythagorasNumber.pfister_problem.variants.upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/a25a41b3e51f6987edeafcc1602e80e6d30e6f05/Proofs/T_PfisterPythagorasNumber_pfister_problem_variants_upper_bound.lean#L1006](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/a25a41b3e51f6987edeafcc1602e80e6d30e6f05/Proofs/T_PfisterPythagorasNumber_pfister_problem_variants_upper_bound.lean#L1006).

> **Pfister's theorem**: every sum of squares in $\mathbb{R}(X_1, \dots, X_n)$ is a sum of $2^n$
> squares [Pfister1995, p. 95]; this is Corollary 1 of Theorem 2 in [Pfister1971]. For positive
> semidefinite polynomials it is [Pfister1967, Theorem 1], the quantitative refinement of Artin's
> theorem `Hilbert17.hilbert_17th_problem` in `FormalConjectures/HilbertProblems/17.lean`.

```lean
theorem pfister_problem.variants.upper_bound (n : ℕ) :
    2 ^ n ∈ pythagorasBounds (MvRatFunc (Fin n) ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/PfisterPythagorasNumber.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PfisterPythagorasNumber.lean#L112).

## `PfisterPythagorasNumber.pfister_problem.variants.cassels`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/a25a41b3e51f6987edeafcc1602e80e6d30e6f05/Proofs/T_PfisterPythagorasNumber_pfister_problem_variants_cassels.lean#L434](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/a25a41b3e51f6987edeafcc1602e80e6d30e6f05/Proofs/T_PfisterPythagorasNumber_pfister_problem_variants_cassels.lean#L434).

> **Cassels' theorem** [Cassels1964], as quoted in Problem 1 of [Pfister1971, §4]:
> $1 + X_1^2 + \dots + X_n^2$ is not a sum of $n$ squares in $\mathbb{R}(X_1, \dots, X_n)$.

```lean
theorem pfister_problem.variants.cassels (n : ℕ) :
    ¬IsSumSqOfLength n (algebraMap (MvPolynomial (Fin n) ℝ) (MvRatFunc (Fin n) ℝ)
      (1 + ∑ i, MvPolynomial.X i * MvPolynomial.X i))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/PfisterPythagorasNumber.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PfisterPythagorasNumber.lean#L122).

## `PfisterPythagorasNumber.pfister_problem.variants.add_one_le`

Proved here.

> The lower bound $n + 1 \le p(\mathbb{R}(X_1, \dots, X_n))$ quoted in Problem 1 of
> [Pfister1971, §4]: $1 + X_1^2 + \dots + X_n^2$ is a sum of $n + 1$ squares but, by Cassels'
> theorem `pfister_problem.variants.cassels`, not of $n$ squares. It is superseded by
> `pfister_problem.variants.lower_bound` for $n \ge 2$.

```lean
theorem pfister_problem.variants.add_one_le (n : ℕ) {p : ℕ}
    (hp : p ∈ pythagorasBounds (MvRatFunc (Fin n) ℝ)) : n + 1 ≤ p
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/PfisterPythagorasNumber.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PfisterPythagorasNumber.lean#L134).

## `PfisterPythagorasNumber.pfister_problem.variants.lower_bound`

Solved: stated here without proof.

> The lower bound $n + 2 \le p(\mathbb{R}(X_1, \dots, X_n))$ for $n \ge 2$ [Pfister1995, p. 97],
> a consequence of the Cassels–Ellison–Pfister theorem [CEP1971]. The hypothesis $n \ge 2$ is
> needed: $p(\mathbb{R}(X)) = 2 < 3$.

```lean
theorem pfister_problem.variants.lower_bound (n : ℕ) (hn : 2 ≤ n) {p : ℕ}
    (hp : p ∈ pythagorasBounds (MvRatFunc (Fin n) ℝ)) : n + 2 ≤ p
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/PfisterPythagorasNumber.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PfisterPythagorasNumber.lean#L149).

## `PfisterPythagorasNumber.pfister_problem.variants.zero`

Textbook result, proved here.

> $p(\mathbb{R}(X_1, \dots, X_n)) = 1$ for $n = 0$, i.e. $p(\mathbb{R}) = 1$: here the bounds $n + 1$
> and $2^n$ of `pfister_problem.variants.add_one_le` and `pfister_problem.variants.upper_bound`
> agree. Compare `isLeast_pythagorasBounds_real`, the same value for `ℝ` itself.

```lean
theorem pfister_problem.variants.zero : IsLeast (pythagorasBounds (MvRatFunc (Fin 0) ℝ)) 1
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/PfisterPythagorasNumber.lean, line 159](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PfisterPythagorasNumber.lean#L159).

## `PfisterPythagorasNumber.pfister_problem.variants.one`

Textbook result, proved here.

> $p(\mathbb{R}(X)) = 2$ [Pfister1995, p. 96]: Pfister's bound gives $p \le 2$, and Cassels'
> theorem `pfister_problem.variants.cassels` gives $p \ge 2$ through
> `pfister_problem.variants.add_one_le`, since $1 + X^2$ is a sum of two squares that is not a
> square in $\mathbb{R}(X)$.

```lean
theorem pfister_problem.variants.one : IsLeast (pythagorasBounds (MvRatFunc (Fin 1) ℝ)) 2
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/PfisterPythagorasNumber.lean, line 170](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PfisterPythagorasNumber.lean#L170).

## `PfisterPythagorasNumber.pfister_problem.variants.two`

Proved here.

> $p(\mathbb{R}(X_1, X_2)) = 4$ [CEP1971], as recorded in [Pfister1971, §4] and [Pfister1995, p. 96]:
> the bounds $n + 2$ and $2^n$ agree when $n = 2$.

```lean
theorem pfister_problem.variants.two : IsLeast (pythagorasBounds (MvRatFunc (Fin 2) ℝ)) 4
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/PfisterPythagorasNumber.lean, line 179](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PfisterPythagorasNumber.lean#L179).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/PfisterPythagorasNumber.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/PfisterPythagorasNumber.lean)
- [IMU scan](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1970.1/ICM1970.1.ocr.pdf)
