---
declaration: section
origin: cited
---

# 290. Relative bicentralizers and modular spectral recovery

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Connes' bicentralizer conjecture for every type III$_{1}$ factor with separable predual and every faithful normal state. More generally, for every inclusion $N\subset M$ of von Neumann algebras with separable preduals admitting a faithful normal conditional expectation, constructs an amenable expected subalgebra $P\subset N$ with $P'\cap c(M)=N'\cap c(M)$, resolving the relative bicentralizer conjecture.

## Expected amenable subalgebras preserving core commutants

We prove that every inclusion $N\subset M$ of von Neumann algebras with separable preduals and a faithful normal conditional expectation contains an expected amenable subalgebra $P\subset N$ such that $P'\cap c(M)=N'\cap c(M)$, where $c(M)$ denotes the continuous core of *M*. This resolves the relative bicentralizer conjecture in this setting.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026.pdf).

## Bounded recovery for modular spectral averages

We prove a bounded spectral recovery theorem for a von Neumann algebra with a faithful normal state whose centralizer consists only of scalars. A positive averaged squared norm for an arbitrary bounded Hilbert-space operator on shrinking modular spectral bands can be recovered on uniformly bounded algebra elements with shrinking spectral support. We apply this theorem to spectral intertwining rigidity and obtain an alternative proof of bicentralizer triviality for type III$_{1}$ factors with separable predual.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/Bounded-recovery-for-modular-spectral-averages-September-23-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

For a faithful normal state with scalar centralizer in the stated standard-space representation, the formalized result converts positive modular spectral averages into uniformly bounded algebra elements. Given unit vectors in shrinking spectral bands around a real number $s$ and a positive limiting symmetric average for a bounded operator $T$, it finds a subsequence of bounded algebra elements whose images under $T$ stay uniformly nonzero and whose spectral bands have four times the original widths. The absolute bicentralizer conjecture is not included.

## Lean: Bounded recovery from modular spectral averages

Stated in [BoundedRecovery.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BoundedRecovery.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem bounded_recovery (S : StandardModularData H) (hscalar : S.ScalarCentralizer)
    (omega : Ultrafilter ℕ) (hfree : (omega : Filter ℕ) ≤ Filter.atTop)
    (T : H →L[ℂ] H) (s : ℝ) (delta : ℕ → ℝ) (hdelta : ∀ n, 0 < delta n)
    (hdelta0 : Tendsto delta atTop (𝓝 0)) (h : ℕ → H) (hunit : ∀ n, ‖h n‖ = 1)
    (hband : ∀ n, S.D.HasSpectralSupport (Icc (s - delta n) (s + delta n)) (h n))
    (hpositive : 0 < Filter.limsup
      (fun n => fixedMean omega (fun t => ‖T (S.D.unitary t (h n))‖ ^ 2)) atTop) :
    RecoveryConclusion S T s delta
```

Its proof is in [lean/OAI/Analysis/ModularRecovery/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/ModularRecovery/Main.lean) or a file it imports further down, which this chapter does not read.

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/290.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/290.md)
