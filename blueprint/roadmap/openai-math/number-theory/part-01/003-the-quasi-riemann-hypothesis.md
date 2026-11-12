---
declaration: section
origin: cited
lean: OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re, OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re, OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re, OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap, OAI.SiegelZeros.WeightedTorusJets.dirichletRealZeroBound_proof
statement: formalized
proof: formalized
---

# 003. The quasi-Riemann hypothesis

3 manuscripts and 5 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that every Dirichlet *L*-function, including $\zeta(s)$, is zero-free in $\Re s\gt 7/8$, resolving the quasi-Riemann hypothesis. The same half-plane is zero-free for every finite-order Hecke *L*-function over $\mathbb Q(\sqrt{-3})$. A companion gives a different proof of the zero-free half-plane $\Re s\gt 11/12$.

## The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s\gt 7/8$

We prove that all finite-order Hecke *L*-functions over $\mathbb Q(\sqrt{-3})$ and all Dirichlet *L*-functions are zero-free in the half-plane $\Re s\gt 7/8$, with the principal pole at *s* = 1 allowed. In particular, the Riemann zeta function is zero-free in this half-plane, proving the quasi-Riemann hypothesis.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf); the Lean below formalizes results from it.

## The Quasi-Riemann Hypothesis (alternate 11/12 proof)

We establish the quasi-Riemann hypothesis by proving that every Dirichlet *L*-function, including Riemann's zeta function, has no zeros in the half-plane $\mathop{\mathrm{Re}}\nolimits s\gt 11/12$. More generally, we prove the same zero-free half-plane for every finite-order Hecke *L*-function over $K=\mathbb Q(\sqrt{-3})$. In particular, this rules out the existence of Landau–Siegel zeros.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf).

## Uniform exclusion of Landau–Siegel zeros

We prove the uniform exclusion of Landau–Siegel zeros. There is an absolute constant *c* > 0 such that every real zero $\beta\in(0,1)$ of every primitive nonprincipal real Dirichlet *L*-function of conductor *q* ≥ 3 satisfies $(1-\beta)\log q\ge c$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The quasi-Riemann hypothesis asks for a fixed zero-free half-plane $\Re s>\theta$ with $\theta<1$. The formalization gives $\theta=7/8$ for the Riemann zeta function and every Dirichlet $L$-function, uniformly over all positive moduli and all characters. It also establishes the same bound for finite-order Hecke $L$-functions over $\mathbb Q(\sqrt{-3})$.

The principal-character poles at $s=1$ are excluded in the Dirichlet and Hecke statements. The paper's later applications are not included.

The formalized result gives a uniform logarithmic exclusion region for Landau–Siegel zeros. There is one constant $c>0$ such that every primitive nonprincipal real Dirichlet character of conductor $q\ge3$ and every real zero $0<\beta<1$ of its $L$-function satisfy $1-\beta\ge c/\log q$.

Both character parities are included. No explicit value of $c$ is given. This excludes real zeros in $1-c/\log q<\beta<1$, but does not rule out real zeros elsewhere in $(0,1)$.

## Lean: Riemann zeta $7/8$ bound

Stated in [QuasiRiemannHypothesis.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/QuasiRiemannHypothesis.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0
```

Proved in [lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean, line 29](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean#L29).

## Lean: Dirichlet $L$-function $7/8$ bound

Stated in [DirichletSevenEighths.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DirichletSevenEighths.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem LFunction_ne_zero_of_seven_eighths_lt_re
    {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ}
    (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
    _root_.DirichletCharacter.LFunction χ s ≠ 0
```

Proved in [lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean, line 19](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean#L19).

## Lean: Finite-order Hecke $L$-function $7/8$ bound

Stated in [HeckeSevenEighths.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HeckeSevenEighths.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem LFunction_ne_zero_of_seven_eighths_lt_re
    (χ : Character) {s : ℂ} (hs : (7 / 8 : ℝ) < s.re)
    (hpole : ¬ (χ.residue = 1 ∧ s = 1)) : LFunction χ s ≠ 0
```

Proved in [lean/OAI/NumberTheory/DirichletL/Hecke/Nonvanishing.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/DirichletL/Hecke/Nonvanishing.lean#L13).

## Lean: Uniform real-zero gap

Stated in [SiegelZeros.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SiegelZeros.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem exists_absolute_real_zero_gap :
    ∃ c : ℝ, 0 < c ∧
      ∀ (q : ℕ) [NeZero q], 3 ≤ q →
      ∀ χ : DirichletCharacter ℂ q,
        χ.IsPrimitive → χ ≠ 1 → (∀ a : ZMod q, (χ a).im = 0) →
        ∀ β : ℝ, 0 < β → β < 1 → χ.LFunction (β : ℂ) = 0 →
          c ≤ (1 - β) * Real.log (q : ℝ)
```

Proved in [lean/OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean#L11).

```lean
theorem WeightedTorusJets.dirichletRealZeroBound_proof :
    ∃ c : ℝ, 0 < c ∧ ∀ (q : ℕ) [NeZero q], 3 ≤ q →
      ∀ χ : DirichletCharacter ℂ q,
        χ.IsPrimitive → χ ≠ 1 → (∀ a : ZMod q, (χ a).im = 0) →
        ∀ β : ℝ,
          (0 < β ∧ β < 1 ∧ DirichletCharacter.LFunction χ (β : ℂ) = 0) →
            c ≤ (1 - β) * Real.log (q : ℝ)
```

Proved in [lean/OAI/NumberTheory/SiegelZeros/Characters/DirichletRealZeroBoundProof.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/SiegelZeros/Characters/DirichletRealZeroBoundProof.lean#L17).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/003.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/003.md)
