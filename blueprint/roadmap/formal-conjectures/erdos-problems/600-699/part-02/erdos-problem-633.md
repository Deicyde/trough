---
declaration: lemma
origin: cited
lean: Erdos633.isCuttable_iff_isSquare_of_linearIndependent, Erdos633.erdos_633, Erdos633.IsSimiliCuttable.of_ne_zero_two_three_five, Erdos633.exists_isSimiliCuttable_iff_ne_zero_two_three_five
statement: formalized
---

# Erdős Problem 633

> *Reference:*
> * [erdosproblems.com/633](https://www.erdosproblems.com/633)
> * [So09] Soifer, Alexander, How Does One Cut a Triangle? I
> * [So09c] Soifer, Alexander, Is there anything beyond the solution?
> * [BLZ26] Beeson, Michael, Laczkovich, Miklós, and Zhang, Yan,
>   [*Solution of Erdős problem 633*](https://arxiv.org/abs/2604.03609).

*Quoted from [FormalConjectures/ErdosProblems/633.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/633.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/633](https://www.erdosproblems.com/633).

The file states 4 research or textbook statements: 4 solved. It also has 4 API statements, counted here but not shown.

## `Erdos633.isCuttable_iff_isSquare_of_linearIndependent`

Solved: stated here without proof.

> A triangle whose side lengths and angles are integrally independent is cuttable only into
> a non-zero square number of congruent triangles. This is proved in [So09c].

```lean
lemma isCuttable_iff_isSquare_of_linearIndependent
    (hTsides : LinearIndependent ℤ
      ![dist (T.points 0) (T.points 1),
        dist (T.points 1) (T.points 2),
        dist (T.points 2) (T.points 0)])
    (hTangles : LinearIndependent ℤ
      ![∠ (T.points 0) (T.points 1) (T.points 2),
        ∠ (T.points 1) (T.points 2) (T.points 0),
        ∠ (T.points 2) (T.points 0) (T.points 1)]) :
    IsCuttable n T ↔ n ≠ 0 ∧ IsSquare n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/633.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/633.lean#L66).

## `Erdos633.erdos_633`

Solved: stated here without proof.

> Which triangles can only be decomposed into a square number of congruent triangles?
>
> Beeson, Laczkovich, and Zhang [BLZ26] classify the triangles that can be tiled only into a square
> number of congruent triangles, settling this problem. The classification is too involved to encode
> in the answer slot here, so the answer is left as `sorry` and the reference records the result.

```lean
lemma erdos_633 : T ∈ erdos_633.answer ↔
    ∀ n, IsCuttable n T → IsSquare n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/633.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/633.lean#L89).

## `Erdos633.IsSimiliCuttable.of_ne_zero_two_three_five`

Solved: stated here without proof.

> Every triangle is simili-cuttable into any number of similar triangles, except 0, 2, 3, 5.
> This is proved in [So09].

```lean
lemma IsSimiliCuttable.of_ne_zero_two_three_five (hn₀ : n ≠ 0) (hn₂ : n ≠ 2) (hn₃ : n ≠ 3)
    (hn₅ : n ≠ 5) : IsSimiliCuttable n T
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/633.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/633.lean#L110).

## `Erdos633.exists_isSimiliCuttable_iff_ne_zero_two_three_five`

Solved: stated here without proof.

> There exists a triangle which isn't simili-cuttable into 0, 2, 3, 5 parts.
> This is proved in [So09].

```lean
lemma exists_isSimiliCuttable_iff_ne_zero_two_three_five :
    ∃ T, ∀ n, IsSimiliCuttable n T ↔ n ≠ 0 ∧ n ≠ 2 ∧ n ≠ 3 ∧ n ≠ 5
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/633.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/633.lean#L116).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/633.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/633.lean)
- [erdosproblems.com/633](https://www.erdosproblems.com/633)
