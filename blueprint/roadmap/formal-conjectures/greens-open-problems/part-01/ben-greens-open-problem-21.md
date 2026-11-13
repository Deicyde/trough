---
declaration: theorem
origin: cited
lean: Green21.green_21, Green21.green_21.variants.fox_kleitman, Green21.green_21.variants.fox_kleitman_sharp, Green21.green_21.variants.fox_kleitman_modular, Green21.green_21.variants.milicevic
statement: formalized
---

# Ben Green's Open Problem 21

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.21)
> - [Ra33] Rado, Richard, *Studien zur Kombinatorik*. Math. Zeit. 36 (1933), 424-480.
> - [FoKl06] Fox, Jacob and Kleitman, Daniel, *On Rado's boundedness conjecture*. J. Combin. Theory
>   Ser. A 113 (2006), no. 1, 84-100.
> - [ElJo23] Ellis, David and Johnson, Robert (editors), *A collection of open problems in
>   celebration of Imre Leader's 60th birthday*. arXiv preprint arXiv:2310.18163 (2023).

*Quoted from [FormalConjectures/GreensOpenProblems/21.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/21.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 4 open and 1 solved. It also has 4 test statements, counted here but not shown.

## `Green21.green_21`

Open: stated without proof.

> Suppose that $a_1, \dots, a_k$ are integers which do not satisfy Rado's condition: thus if
> $\sum_{i \in I} a_i = 0$ then $I = \emptyset$. It then follows from Rado's theorem that the
> equation $a_1x_1 + \cdots + a_kx_k = 0$ is not partition regular. Write $c(a_1, \dots, a_k)$ for
> the least number of colours required in order to colour $\mathbb{N}$ so that there is no
> monochromatic solution to $a_1x_1 + \cdots + a_kx_k = 0$. Is $c(a_1, \dots, a_k)$ bounded in
> terms of $k$ only?
>
> This problem, which is known as Rado's boundedness conjecture, dates back to 1933 [Ra33]. It is
> open for all $k \geq 4$.

```lean
theorem green_21 : ∃ B : ℕ → ℕ, ∀ (k : ℕ) (a : Fin k → ℤ),
    ¬ RadoCondition a → minColours a ≤ B k
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/21.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/21.lean#L78).

## `Green21.green_21.variants.fox_kleitman`

Solved: stated here without proof.

> The answer was shown to be affirmative for $k = 3$ by Fox and Kleitman [FoKl06], who showed that
> $c(a_1, a_2, a_3) \leq 24$.

```lean
theorem green_21.variants.fox_kleitman (a : Fin 3 → ℤ) (ha : ¬ RadoCondition a) :
    minColours a ≤ 24
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/21.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/21.lean#L87).

## `Green21.green_21.variants.fox_kleitman_sharp`

Open: stated without proof.

> Green [Gr24] is not sure that the constant $24$ of [FoKl06] is sharp, and remarks that it might
> be interesting to determine the sharp constant.
>
> The largest value of $c(a_1, a_2, a_3)$ is attained, since by `green_21.variants.fox_kleitman`
> the values form a non-empty set of naturals bounded above by $24$.

```lean
theorem green_21.variants.fox_kleitman_sharp :
    IsGreatest {c | ∃ a : Fin 3 → ℤ, ¬ RadoCondition a ∧ minColours a = c}
      green_21.variants.fox_kleitman_sharp.answer
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/21.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/21.lean#L101).

## `Green21.green_21.variants.fox_kleitman_modular`

Open: stated without proof.

> A question [FoKl06, Conjecture 5] of Fox and Kleitman, which they call a 'modular analogue' of
> Rado's Boundedness Conjecture. Let $k > 0$, let $p$ be a prime, and suppose that
> $a_1, \dots, a_k$ are integers with $\sum_{i \in I} a_i \equiv 0 \pmod p$ only when
> $I = \emptyset$. Does there exist
> an $f(k)$-colouring of $(\mathbb{Z}/p\mathbb{Z})^*$ with no monochromatic solution to
> $a_1x_1 + \cdots + a_kx_k = 0$? This seems to be open even when $k = 3$; Green [Gr24] suspects
> the answer may be negative.
>
> The point of the question is that the number of colours $f(k)$ must not depend on $p$.
>
> The arity $k$ is required to be positive, as in [FoKl06]: for $k = 0$ the empty tuple is a
> monochromatic solution with sum $0$ for every colouring, so no $f(0)$ could work.

```lean
theorem green_21.variants.fox_kleitman_modular : ∃ f : ℕ → ℕ,
    ∀ (k p : ℕ), 0 < k → p.Prime → ∀ a : Fin k → ℤ,
      (∀ I : Finset (Fin k), (p : ℤ) ∣ ∑ i ∈ I, a i → I = ∅) →
      ∃ col : (ZMod p)ˣ → Fin (f k), ∀ x : Fin k → (ZMod p)ˣ,
        (∀ i j, col (x i) = col (x j)) → ∑ i, (a i : ZMod p) * (x i : ZMod p) ≠ 0
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/21.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/21.lean#L121).

## `Green21.green_21.variants.milicevic`

Open: stated without proof.

> Milićević [ElJo23, Conjecture 11.1] conjectures the following 2-adic variant. For any
> $k \in \mathbb{N}$, there exists $K = K(k)$ such that the following is true. Let $r$ be a
> positive integer, and let $a_1, \dots, a_k \in \mathbb{Z}/2^r\mathbb{Z}$. Let $d$ be the largest
> integer such that $\sum_{i \in I} a_i \equiv 0 \pmod{2^d}$ for some non-empty subset
> $I \subset [k]$. Then there is a $K$-colouring of $\mathbb{Z}/2^r\mathbb{Z}$ such that all
> monochromatic solutions $x = (x_1, \dots, x_k)$ to the equation
> $a_1x_1 + \cdots + a_kx_k = 0$ satisfy $x_i \equiv 0 \pmod{2^{r-d}}$ for all $i = 1, \dots, k$.
>
> Milićević remarks that, if true, this would imply the Rado boundedness conjecture by a
> compactness argument.

```lean
theorem green_21.variants.milicevic : ∀ k : ℕ, ∃ K : ℕ, ∀ r : ℕ, 0 < r →
    ∀ a : Fin k → ZMod (2 ^ r), ∃ col : ZMod (2 ^ r) → Fin K,
      ∀ x : Fin k → ZMod (2 ^ r), (∀ i j, col (x i) = col (x j)) →
        ∑ i, a i * x i = 0 → ∀ i, 2 ^ (r - maxDepth a) ∣ (x i).val
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/21.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/21.lean#L151).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/21.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/21.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.21)
