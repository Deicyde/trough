---
declaration: theorem
origin: cited
lean: Erdos482.erdos_482, Erdos482.erdos_482.variants.stoll_general, Erdos482.erdos_482.variants.binary_explicit, Erdos482.erdos_482.variants.stoll_explicit
statement: formalized
---

# Erdős Problem 482

> *References:*
> - [erdosproblems.com/482](https://www.erdosproblems.com/482)
> - [GrPo70] Graham, R. L. and Pollak, H. O., Note on a nonlinear recurrence related to {$\surd 2$}. Math. Mag. (1970), 143-145.
> - [St05] Stoll, Th., On families of nonlinear recurrences related to digits. J. Integer Seq. (2005), Article 05.3.2, 8.
> - [St06] Stoll, Thomas, On a problem of Erd\H{o}s and Graham concerning digits. Acta Arith. (2006), 89-100.
> - [RaGi91] Rabinowitz, S. and Gilbert, P., A nonlinear recurrence yielding binary digits. Math. Mag.
>   64 (1991), 168-171.
>
> A formal Lean proof is given in an external repository,
> [`gotrevor/lean-gallery`](https://github.com/gotrevor/lean-gallery), formalized by Trevor Morris with
> Claude Code.

*Quoted from [FormalConjectures/ErdosProblems/482.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/482.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/482](https://www.erdosproblems.com/482).

The file states 4 research or textbook statements: 4 solved.

## `Erdos482.erdos_482`

Solved: stated here; a Lean proof is at [https://github.com/gotrevor/lean-gallery/blob/a28a487968d989b24c9dde9b1958aa5b92c6fccb/LeanGallery/NumberTheory/Erdos482/Statement.lean#L46-L49](https://github.com/gotrevor/lean-gallery/blob/a28a487968d989b24c9dde9b1958aa5b92c6fccb/LeanGallery/NumberTheory/Erdos482/Statement.lean#L46-L49).

> Define a sequence by $a_1=1$ and $$a_{n+1}=\lfloor\sqrt{2}(a_n+1/2)\rfloor$$ for $n\geq 1$.
> The difference $a_{2n+1}-2a_{2n-1}$ is the $n$th digit in the binary expansion of $\sqrt{2}$.
>
> Find similar results for $\theta=\sqrt{m}$, and other algebraic numbers.
>
> The result for $\sqrt{2}$ was obtained by Graham and Pollak [GrPo70]. The problem statement is
> open-ended, but presumably Erdős and Graham would have been satisfied with the wide-ranging
> generalisations of Stoll ([St05] and [St06]).
>
> The binary expansion is $\sqrt{2} = 1.0110101\ldots$, and the $n$th digit counts the leading $1$ as
> digit $1$.  It is stated with Mathlib's `Real.digits`: the $n$th digit of $\sqrt{2}$ is digit $n - 1$
> of $\sqrt{2}/2 = 0.10110101\ldots$, that is $\lfloor \sqrt{2} \cdot 2^{n-1} \rfloor \bmod 2$.  The
> second conjunct records that these digits are the binary expansion: they reconstruct $\sqrt{2}/2$.

```lean
theorem erdos_482 :
    (∀ n : ℕ, 1 ≤ n →
      (a (2 * n + 1) : ℤ) - 2 * a (2 * n - 1) = (Real.digits (√2 / 2) 2 (n - 1) : ℕ)) ∧
      Real.ofDigits (Real.digits (√2 / 2) 2) = √2 / 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/482.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/482.lean#L73).

## `Erdos482.erdos_482.variants.stoll_general`

Solved: stated here; a Lean proof is at [https://github.com/gotrevor/lean-gallery/blob/a834bbad2f36eedcc16066b2bc4da49f98ab5b85/LeanGallery/NumberTheory/Erdos482/Statement.lean#L64-L67](https://github.com/gotrevor/lean-gallery/blob/a834bbad2f36eedcc16066b2bc4da49f98ab5b85/LeanGallery/NumberTheory/Erdos482/Statement.lean#L64-L67).

> Stoll's general answer to the open-ended part [St05]: for every real $w > 0$ and every base
> $g \ge 2$, there are parameters $a$, $b$, and $\varepsilon$, with $ab = g$, such that the
> corresponding Graham–Pollak-type recurrence reads the base-$g$ digits of $w$.
>
> The mantissa normalization is $w / g^{\lfloor \log_g w \rfloor}$, so the right-hand side is the
> standard Mathlib base-$g$ digit of the normalized expansion.

```lean
theorem erdos_482.variants.stoll_general (g : ℕ) [NeZero g] (hg : 2 ≤ g) (w : ℝ) (hw : 0 < w) :
    ∃ a b ε : ℝ, a * b = g ∧
      ∀ n : ℕ, 1 ≤ n →
        generalRecurrence g a b ε (2 * n) - g * generalRecurrence g a b ε (2 * n - 2) =
          (Real.digits (w / (g : ℝ) ^ ⌊Real.logb g w⌋ * (g : ℝ) ^ (n - 1) / g) g 0 : ℕ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/482.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/482.lean#L89).

## `Erdos482.erdos_482.variants.binary_explicit`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/33a6b9a285cb64ac276ce4d0b3a4111b82c972b6/src/latest/ErdosProblems/Erdos482.lean#L323-L332](https://github.com/plby/lean-proofs/blob/33a6b9a285cb64ac276ce4d0b3a4111b82c972b6/src/latest/ErdosProblems/Erdos482.lean#L323-L332).

> The explicit binary answer to the open-ended part [RaGi91], [St05]: for every normalized real
> $t \in [1, 2)$, the recurrence with coefficients $\alpha(t) = 2(t+1)/(t+2)$ and
> $\beta(t) = (t+2)/(t+1)$ reads off the binary digits of $t$, and those digits reconstruct $t$.
> Unlike `erdos_482.variants.stoll_general`, the coefficients are given, not merely shown to exist.

```lean
theorem erdos_482.variants.binary_explicit (t : ℝ) (ht1 : 1 ≤ t) (ht2 : t < 2) :
    (∀ n, 1 ≤ n →
        stollBinary t (2 * n) - 2 * stollBinary t (2 * n - 2) = (binaryDigit t n).val) ∧
      Real.ofDigits (fun k ↦ binaryDigit t (k + 2)) = t - 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/482.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/482.lean#L125).

## `Erdos482.erdos_482.variants.stoll_explicit`

Solved: stated here without proof.

> The explicit base-$g$ construction in Stoll [St05, Theorem 1.3]. For a normalized
> $t \in [1,g)$, take $a = g/((g-1)(t+g))$ and $b = (g-1)(t+g)$. Every parameter
> $-1/g \le \varepsilon < (g+1)(g-2)/g$ gives the same significant digits of $t$.
>
> The sequence is indexed from zero, so the difference at $2n+2$ and $2n$ gives digit $n$,
> including the leading digit at $n=0$. The floor difference uses the terminating expansion
> when $t$ has two base-$g$ expansions.

```lean
theorem erdos_482.variants.stoll_explicit (g : ℕ) (hg : 2 ≤ g) (t : ℝ)
    (ht : 1 ≤ t) (htg : t < g) (ε : ℝ)
    (hεlo : -1 / (g : ℝ) ≤ ε)
    (hεhi : ε < ((g : ℝ) + 1) * ((g : ℝ) - 2) / g) :
    let a := (g : ℝ) / (((g : ℝ) - 1) * (t + g))
    let b := ((g : ℝ) - 1) * (t + g)
    ∀ n : ℕ,
      generalRecurrence g a b ε (2 * n + 2) -
          (g : ℤ) * generalRecurrence g a b ε (2 * n) =
        ⌊t * (g : ℝ) ^ n⌋ - (g : ℤ) * ⌊t * (g : ℝ) ^ n / g⌋
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/482.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/482.lean#L139).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/482.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/482.lean)
- [erdosproblems.com/482](https://www.erdosproblems.com/482)
