---
declaration: theorem
origin: cited
lean: Kakeya.kakeya_set_conjecture, Kakeya.kakeya_2d, Kakeya.kakeya_3d, Kakeya.kakeya_finite
statement: formalized
---

# Kakeya problem

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Kakeya_set)

*Quoted from [FormalConjectures/Wikipedia/Kakeya.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Kakeya.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 1 test statement, counted here but not shown.

## `Kakeya.kakeya_set_conjecture`

Open: stated without proof.

> The Kakeya set conjecture: Kakeya sets in $\mathbb{R}^n$ have Hausdorff dimension $n$.

```lean
theorem kakeya_set_conjecture (n : ℕ) (hn : n > 0) :
    KakeyaSetConjectureDim n
```

Category `research open`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/Wikipedia/Kakeya.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Kakeya.lean#L62).

## `Kakeya.kakeya_2d`

Solved: stated here without proof.

> The two-dimensional case, proved by Davies [Da71].
>
> [Da71] Davies, R. O., _Some remarks on the Kakeya problem_. Math. Proc. Cambridge Philos. Soc. 69 (1971), no. 3, 417–421.

```lean
theorem kakeya_2d : KakeyaSetConjectureDim 2
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/Wikipedia/Kakeya.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Kakeya.lean#L73).

## `Kakeya.kakeya_3d`

Solved: stated here without proof.

> The three-dimensional case, proved by Wang, Zahl [WaZa25].
>
> [WaZa25] Wang, H. and Zahl, J., _Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions_. arXiv preprint, arXiv:2502.17655, 2025.

```lean
theorem kakeya_3d : KakeyaSetConjectureDim 3
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/Wikipedia/Kakeya.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Kakeya.lean#L83).

## `Kakeya.kakeya_finite`

Solved: stated here without proof.

> The finite field Kakeya conjecture asserts that any Kakeya set in `𝔽_qⁿ` has size at
> least `c_n · qⁿ` for some constant `c_n` depending only on `n`.
> This was first proved by Dvir [Dv08]. The best known bound to date, due to Bukh and Chao [BuCh21],
> establishes that any Kakeya set in `𝔽_qⁿ` has size at least `qⁿ / (2 - 1/q)^(n - 1)`.
> The dimension is positive, as in `kakeya_set_conjecture`; for `n = 0` the empty set is a Kakeya
> set and the bound would read `1 ≤ 0`.
>
> [Dv08] Dvir, Z., _On the size of Kakeya sets in finite fields_. Journal of the American Mathematical Society 22 (2009), no. 4, 1093–1097.
> [BuCh21] Bukh, B. and Chao, T.-W., _Sharp density bounds on the finite field Kakeya problem_. Discrete Analysis 26 (2021), 9 pp.

```lean
theorem kakeya_finite {F : Type*} [Field F] [Fintype F] {n : ℕ} (hn : 0 < n)
    (K : Finset (Fin n → F)) (hK : IsKakeyaFinite K) :
    card F ^ n / (2 - 1 / card F : ℚ) ^ (n - 1) ≤ K.card
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/Kakeya.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Kakeya.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Kakeya.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Kakeya.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Kakeya_set)
