---
declaration: section
origin: cited
lean: OAI.TotientAsymptotic.totient_asymptotic_formula, OAI.TotientAsymptotic.weighted_totient_asymptotic, OAI.TotientAsymptotic.weighted_totient_one_two, OAI.TotientAsymptotic.coefficient_nonnegative, OAI.TotientAsymptotic.companion_zero_case
statement: formalized
proof: formalized
---

# 024. An asymptotic formula for the number of totients

1 manuscript and 5 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives an asymptotic equivalent for the number $V(x)$ of distinct totient values up to *x*, with a positive bounded phase-dependent factor determined by convergent arithmetic approximations. In particular, $V(cx)/V(x)\to c$ for every fixed *c* > 0, answering Erdős and Hall’s scaling question.

## An asymptotic formula for the number of totients

Let $V(x)$ count the distinct values of Euler's totient function up to *x*. We give an explicit asymptotic equivalent for $V(x)$. Its coefficient is a uniform limit of functions defined from finite arithmetic data. We also prove that $V(cx)/V(x)\to c$ as $x\to\infty$ for every fixed *c* > 0, answering a question of Erdős and Hall.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/An-asymptotic-formula-for-the-number-of-totients-September-25-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

Let $V(x)$ count the distinct values of Euler's totient function up to $x$. The formalization constructs the paper's explicit positive main term from finite arithmetic approximants and proves that their ratio tends to one. In particular, $V(cx)/V(x)\to c$ for every fixed $c>0$, answering the Erdős–Hall regular-variation question.

The formalization also gives asymptotics for totients $v\le x$ whose least preimage $\ell(v)=\min\{n\ge1:\varphi(n)=v\}$ lies between $kx$ and $(k+1)x$. The associated coefficient is positive under the stated existence condition; when no totient $d$ satisfies $kd<\ell(d)$, the count and coefficient are identically zero. The cases $k=1,2$ have positive coefficients.

## Lean: Totient-count asymptotics and regular variation

Stated in [TotientAsymptotic.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TotientAsymptotic.lean).

```lean
theorem totient_asymptotic_formula
    :
    TendstoUniformlyOn (fun H => AH H (fun _ => 1)) (A (fun _ => 1))
      atTop (Set.Ico (0 : ℝ) 1) ∧
    (∃ cMinus cPlus : ℝ, 0 < cMinus ∧ ∀ s ∈ Set.Ico (0 : ℝ) 1,
      cMinus ≤ A (fun _ => 1) s ∧ A (fun _ => 1) s ≤ cPlus) ∧
    Tendsto (fun x => V x/mainTerm x) atTop (nhds 1) ∧
    ∀ c : ℝ, 0 < c → Tendsto (fun x => V (c*x)/V x) atTop (nhds c)
```

Proved in [lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean#L12).

```lean
theorem weighted_totient_asymptotic
    (k : ℕ) (hk : 1≤k) :
    TendstoUniformlyOn (fun H => AH H (fk k)) (A (fk k)) atTop (Set.Ico (0 : ℝ) 1) ∧
    Tendsto (fun x => normalizedCount (N k) x-A (fk k) (theta x)) atTop (nhds 0) ∧
    ((∃ d : ℕ, IsTotient d ∧ k*d<ell d) →
      ∃ cMinus cPlus : ℝ, 0<cMinus ∧ 0<cPlus ∧
        (∀ s∈Set.Ico (0 : ℝ) 1, cMinus≤A (fk k) s ∧ A (fk k) s≤cPlus) ∧
        Tendsto (fun x => N k x/(tupleNormalization x*A (fk k) (theta x))) atTop (nhds 1) ∧
        ∀ᶠ x : ℝ in atTop, (cMinus/cPlus)*V x≤N k x ∧ N k x≤V x) ∧
    ((¬∃ d : ℕ, IsTotient d ∧ k*d<ell d) →
      (∀ x : ℝ, 0<x → N k x=0) ∧ (∀ s∈Set.Ico (0 : ℝ) 1, A (fk k) s=0))
```

Proved in [lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean#L23).

```lean
theorem weighted_totient_one_two
    :
    ∀ k∈({1,2} : Finset ℕ), ∃ c : ℝ, 0<c ∧
      ∀ s∈Set.Ico (0 : ℝ) 1, c≤A (fk k) s
```

Proved in [lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean, line 37](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean#L37).

```lean
theorem coefficient_nonnegative (H : ℕ) {s : ℝ}
    (hs : s ∈ Set.Ico (0 : ℝ) 1) : 0 ≤ AH H (fun _ => 1) s
```

Proved in [lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean, line 44](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean#L44).

## Lean: Exact zero case for the companion totient counts

Stated in [TotientCompanionZero.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TotientCompanionZero.lean).

```lean
theorem companion_zero_case (k : ℕ) (_hk : 0 < k)
    (hno : ¬ ∃ d : ℕ, IsTotient d ∧ k*d < ell d) :
    (∀ x : ℝ, 0 < x → N k x = 0) ∧
    (∀ s ∈ Set.Ico (0 : ℝ) 1, A (fk k) s = 0)
```

Proved in [lean/OAI/NumberTheory/TotientAsymptotic/Companion.lean, line 87](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/TotientAsymptotic/Companion.lean#L87).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/024.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/024.md)
