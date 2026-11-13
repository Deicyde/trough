---
declaration: section
origin: cited
lean: OAI.Problem335.main
statement: formalized
proof: formalized
---

# 135. Homogeneous depth-five lower bounds for iterated matrix multiplication

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Over every characteristic-zero field, the $(1,1)$ entry of a product of *n* independent $n\times n$ variable matrices requires $n^{\Theta(\sqrt n)}$ gates in homogeneous depth-five sum–product circuits. This sharp bound allows shared gates and bottom linear forms involving all variables.

## Homogeneous depth-five lower bounds for iterated matrix multiplication

Let $\mathop{\mathrm{IMM}}\nolimits _{n,n}$ be the $(1,1)$ entry of a product of *n* independent $n\times n$ matrices of variables. Over every field of characteristic zero, every syntactically homogeneous $\Sigma\Pi\Sigma\Pi\Sigma$ circuit computing $\mathop{\mathrm{IMM}}\nolimits _{n,n}$ has at least $n^{\sqrt n/400}$ gates for all sufficiently large *n*, with an absolute threshold independent of the field. Bottom linear forms may have arbitrary support, and arbitrary finite fan-in, fan-out, and gate sharing are allowed. Over every field, a block expansion gives such circuits with at most $n^{\sqrt n+4}$ gates for *n* ≥ 2. Thus the gate complexity over characteristic-zero fields is $n^{\Theta(\sqrt n)}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

Let $\mathrm{IMM}_{n,n}$ be the $(1,1)$ entry of the product of $n$ independent $n\times n$ variable matrices. The formalization proves that, over every characteristic-zero field, syntactically homogeneous depth-five $\Sigma\Pi\Sigma\Pi\Sigma$ circuits computing this polynomial require at least $n^{\sqrt n/400}$ gates for all sufficiently large $n$, with a threshold independent of the field. Arbitrary bottom support, finite fan-in and fan-out, and sharing are allowed.

It also gives, over every field and for $n\ge2$, circuits with at most $n^{\sqrt n+4}$ gates. These are the lower and upper bounds selected from the paper.

## Lean: Homogeneous depth-five bounds for iterated matrix multiplication

```lean
theorem main :
    (∃ threshold : ℕ, ∀ size : ℕ, threshold ≤ size →
      ∀ circuit : Depth5Circuit ℂ size, circuitValue circuit = imm ℂ size →
        (size : ℝ) ^ (Real.sqrt (size : ℝ) / 400) ≤ (circuitSize circuit : ℝ)) ∧
    (∃ threshold : ℕ, ∀ (FieldType : Type u) [Field FieldType] [CharZero FieldType],
      ∀ size : ℕ, threshold ≤ size → ∀ circuit : Depth5Circuit FieldType size,
        circuitValue circuit = imm FieldType size →
          (size : ℝ) ^ (Real.sqrt (size : ℝ) / 400) ≤ (circuitSize circuit : ℝ)) ∧
    (∀ (FieldType : Type u) [Field FieldType] (size : ℕ), 2 ≤ size →
      ∃ circuit : Depth5Circuit FieldType size, circuitValue circuit = imm FieldType size ∧
        circuitSize circuit ≤ upperGateBound size ∧
        (upperGateBound size : ℝ) ≤ (size : ℝ) ^ (Real.sqrt (size : ℝ) + 4))
```

Stated in [DepthFive.lean, line 118](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DepthFive.lean#L118). Proved in [lean/OAI/Algebra/DepthFive/Bounds.lean, line 31](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/DepthFive/Bounds.lean#L31).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/135.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/135.md)
