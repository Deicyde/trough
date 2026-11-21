---
declaration: theorem
origin: cited
lean: Green27.green_27.equivalent, Green27.green_27.lower, Green27.green_27.upper, Green27.green_27.variants.lower_be23, Green27.green_27.variants.lower_cy26, Green27.green_27.variants.lower_he26_hy26, Green27.green_27.variants.upper_be23, Green27.green_27.variants.previous_lower, Green27.green_27.variants.previous_upper
statement: formalized
---

# Green's Open Problem 27

> References:
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.27)
> - [Be23] Bedert, Benjamin. "On unique sums in Abelian groups." Combinatorica 44.2 (2024): 269-298.
> - [CY26] Cao, Jiao-Long, and Ye Yuan. "A Second-Logarithm Lower Bound for Sets with No Unique
>   Sums." arXiv preprint arXiv:2608.06728 (2026).
> - [He26] He, Xinjie. "A near-quadratic lower bound for sets with no unique sums." Working draft
>   (July 21, 2026):
>   https://github.com/xinjiegit/ben_27_formalization/blob/f70352964007662e97a810c880abbfea1e2ea262/NUS_edited.tex.
>   Its Lean 4 proof is registered as
>   [PALOMAR-2026-08-18-000003](https://palomar-registry.org/entry.html?id=PALOMAR-2026-08-18-000003&version=1).
> - [HY26] Hou, Jianfeng, and Kai Yang. "A near-quadratic lower bound for sets with no unique sums."
>   arXiv preprint arXiv:2610.09349 (2026).
> - [St76] Straus, E. G. "Differences of residues (mod p)." Journal of Number Theory 8.1 (1976): 40-42.

*Quoted from [FormalConjectures/GreensOpenProblems/27.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/27.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 9 research or textbook statements: 2 open and 7 solved.

## `Green27.green_27.equivalent`

Open: stated without proof.

> What is the size of the smallest set $A \subset \mathbb{Z} / p\mathbb{Z}$ (with at least two elements)
> for which no element in the sumset $A + A$ has a unique representation?

```lean
theorem green_27.equivalent :
  green_27.equivalent.answer ~[primesAtTop] m
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/27.lean#L70).

## `Green27.green_27.lower`

Solved: stated here without proof.

> Propose a better lower bound along primes.
>
> Cao and Yuan [CY26, Theorem 1.1] prove $m(p) \gg \log p \log \log p$. This beats `lowerBest`,
> since $\sqrt{\log \log \log p} / \log \log \log \log p = o(\log \log p)$.
>
> Xinjie He [He26, Theorem 1.2] and Hou and Yang [HY26, Theorem 1.1] prove the stronger bound
> $m(p) \gg (\log p / \log \log p)^2$. He's proof is formalised in Lean, see
> `green_27.variants.lower_he26_hy26`. Together with `green_27.variants.upper_be23`, this lower bound
> gives $m(p) = (\log p)^{2 + o(1)}$. The exact order of $m(p)$ remains open.

```lean
theorem green_27.lower :
    (lowerBest =o[primesAtTop] green_27.lower.answer) ∧ (green_27.lower.answer =O[primesAtTop] m)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/27.lean#L86).

## `Green27.green_27.upper`

Open: stated without proof.

> Propose a better upper bound along primes.

```lean
theorem green_27.upper :
    (green_27.upper.answer =o[primesAtTop] upperBest) ∧ (m =O[primesAtTop] green_27.upper.answer)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/27.lean#L95).

## `Green27.green_27.variants.lower_be23`

Solved: stated here without proof.

> We have $m(p) \geq \omega(p) \log p$ for some function $\omega(p)$ tending to infinity [Be23, Theorem 3].

```lean
theorem green_27.variants.lower_be23 :
  ∃ ω : ℕ → ℝ, Tendsto ω primesAtTop atTop ∧
    ∀ᶠ p in primesAtTop,
      ω p * Real.log (p : ℝ) ≤ m p
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/27.lean#L104).

## `Green27.green_27.variants.lower_cy26`

Solved: stated here without proof.

> Lower bound: $\log p \log \log p \ll m(p)$ [CY26, Theorem 1.1].

```lean
theorem green_27.variants.lower_cy26 :
  (fun p ↦ Real.log (p : ℝ) * Real.log (Real.log (p : ℝ))) =O[primesAtTop] m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/27.lean#L112).

## `Green27.green_27.variants.lower_he26_hy26`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-08-18-000003](https://palomar-registry.org/entry.html?id=PALOMAR-2026-08-18-000003).

> Lower bound: $(\log p / \log \log p)^2 \ll m(p)$ [He26, Theorem 1.2], [HY26, Theorem 1.1].
> The linked formal proof is He's.

```lean
theorem green_27.variants.lower_he26_hy26 :
  ∃ c > (0 : ℝ), ∀ᶠ p : ℕ in primesAtTop,
    c * (Real.log (p : ℝ) / Real.log (Real.log (p : ℝ))) ^ 2 ≤ m p
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/27.lean#L120).

## `Green27.green_27.variants.upper_be23`

Solved: stated here; a Lean proof is at [https://github.com/mkwatson/unique-sums-notes/blob/d4383f93a52e3a916ccce78d5fb7739c3bf3dabc/Green27Upper/Theorem.lean#L26](https://github.com/mkwatson/unique-sums-notes/blob/d4383f93a52e3a916ccce78d5fb7739c3bf3dabc/Green27Upper/Theorem.lean#L26).

> Upper bound: $m(p) \ll (\log p)^2$ [Be23, Theorem 5].

```lean
theorem green_27.variants.upper_be23 :
  m =O[primesAtTop] upperBest
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/27.lean#L129).

## `Green27.green_27.variants.previous_lower`

Solved: stated here without proof.

> Previous best-known lower bound $\log p \ll m(p)$ from [St76].

```lean
theorem green_27.variants.previous_lower :
  (fun p ↦ Real.log (p : ℝ)) =O[primesAtTop] m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/27.lean#L135).

## `Green27.green_27.variants.previous_upper`

Solved: stated here without proof.

> Previous best-known upper bound $m(p) \ll \sqrt{p}$ from [Be23].

```lean
theorem green_27.variants.previous_upper :
  m =O[primesAtTop] (fun p ↦ Real.sqrt (p : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/27.lean#L141).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/27.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/27.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.27)
