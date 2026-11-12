---
declaration: section
origin: cited
lean: OAI.LittleFinitistic.Main.exists_counterexample, OAI.LittleFinitistic.extreme_left_right_asymmetry
statement: formalized
proof: formalized
---

# 198. A counterexample to finitistic-dimension finiteness

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a finite-dimensional complex algebra whose finite-dimensional modules have unbounded finite projective dimensions. This disproves the little finitistic-dimension conjecture.

## An algebra of infinite little finitistic dimension

We construct a finite-dimensional complex algebra whose finite-dimensional modules have unbounded finite projective dimensions. This disproves the little finitistic-dimension conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The little finitistic-dimension conjecture predicts that finitely generated modules of finite projective dimension over a fixed finite-dimensional algebra have bounded projective dimensions. The formalized counterexample is a finite-dimensional complex algebra with a finitely generated module of projective dimension at least $2m-2$ and still finite for every $m\ge1$.

A separate formalized result gives a finite-dimensional complex algebra whose little and big finitistic dimensions are infinite on the left and zero on the right. Injectives fail to generate its unbounded derived category on the left and generate it on the right.

## Lean: Infinite little finitistic dimension

Stated in [LittleFinitistic.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LittleFinitistic.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem exists_counterexample :
    ∃ (A : Type) (_ : Ring A) (_ : Algebra ℂ A),
      FiniteDimensional ℂ A ∧ littleFinitisticDimension A = ⊤ ∧
        ∀ m : ℕ, 0 < m → ∃ N : ModuleCat.{0} A, Module.Finite A N ∧
          ((2*m-2 : ℕ) : WithBot ℕ∞) ≤ projectiveDimension N ∧
            projectiveDimension N < ⊤
```

Proved in [lean/OAI/Algebra/Finitistic/Main.lean, line 44](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/Finitistic/Main.lean#L44).

## Lean: Left/right finitistic-dimension asymmetry

Stated in [FinitisticAsymmetry.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FinitisticAsymmetry.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem extreme_left_right_asymmetry :
    ∃ (Λ : Type) (_ : Ring Λ) (_ : Algebra ℂ Λ),
      FiniteDimensional ℂ Λ ∧
      littleFinitisticDimension Λ = ⊤ ∧ bigFinitisticDimension Λ = ⊤ ∧
      littleFinitisticDimension Λᵐᵒᵖ = 0 ∧ bigFinitisticDimension Λᵐᵒᵖ = 0 ∧
      ¬ InjectivesGenerate Λ ∧ InjectivesGenerate Λᵐᵒᵖ
```

Proved in [lean/OAI/Algebra/FinitisticAsymmetry/Main.lean, line 48](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/FinitisticAsymmetry/Main.lean#L48).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/198.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/198.md)
