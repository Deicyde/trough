---
declaration: theorem
origin: cited
lean: MovingSofa.GerversSofa.ABφθSpec.existsUnique, MovingSofa.isMovingSofa_gerversSofa, MovingSofa.sofaConstant_eq, MovingSofa.sofaConstant_eq_volume_gerversSofa, MovingSofa.volume_eq_sofaConstant_iff_congruent_gerversSofa, MovingSofa.RomiksSofa.existsUnique_X, MovingSofa.RomiksSofa.existsUnique_Y, MovingSofa.romiksSofa_area_le_ambidextrousSofaConstant, MovingSofa.ambidextrousSofaConstant_eq_romiksSofa_area
statement: formalized
---

# Moving Sofa Problem

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Moving_sofa_problem)
> - [Ge92] Gerver, J. L., _On moving a sofa around a corner_. Geometriae Dedicata 42.3 (1992): 267-283.
> - [Ro18] Romik, D. _Differential equations and exact solutions in the moving sofa problem_. Experimental mathematics 27.3 (2018): 316-330.
> - [Ba24] Baek, J. _Optimality of Gerver's Sofa_. arXiv preprint arXiv:2411.19826 (2024).

*Quoted from [FormalConjectures/Wikipedia/MovingSofa.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MovingSofa.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 9 research or textbook statements: 1 open, 5 solved and 3 textbook results. It also has 7 test statements and 1 API statement, counted here but not shown.

## `MovingSofa.GerversSofa.ABφθSpec.existsUnique`

Textbook result, stated without proof. A Lean proof is at [https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Defs.lean#L173](https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Defs.lean#L173); a Lean proof is at [https://github.com/dawidmtrela-dotcom/GerverSofaLean/blob/v1.0.0/GerverSofa/KernelOnly/PartE/E24KC6KernelFinalClosure.lean](https://github.com/dawidmtrela-dotcom/GerverSofaLean/blob/v1.0.0/GerverSofa/KernelOnly/PartE/E24KC6KernelFinalClosure.lean).

> There exist unique constants $A$, $B$, $\varphi$, and $\theta$ satisfying the spec.

```lean
theorem ABφθSpec.existsUnique : ∃! ABφθ : ℝ × ℝ × ℝ × ℝ,
    ABφθSpec ABφθ.1 ABφθ.2.1 ABφθ.2.2.1 ABφθ.2.2.2
```

Category `textbook`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 164](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MovingSofa.lean#L164).

## `MovingSofa.isMovingSofa_gerversSofa`

Solved: stated here; a Lean proof is at [https://github.com/dawidmtrela-dotcom/GerverSofaLean/releases/tag/v1.1.0](https://github.com/dawidmtrela-dotcom/GerverSofaLean/releases/tag/v1.1.0); a Lean proof is at [https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L20](https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L20); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L161-L168](https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L161-L168); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L120-L121](https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L120-L121).

> Gerver's concrete sofa admits a valid hallway motion.

```lean
theorem isMovingSofa_gerversSofa : ∃ m, IsMovingSofa gerversSofa m
```

Category `research solved`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 212](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MovingSofa.lean#L212).

## `MovingSofa.sofaConstant_eq`

Solved: stated here; a Lean proof is at [https://github.com/deancureton/MovingSofa/blob/a0753860f1d2b4424e059c35e64ad611be71a415/MovingSofaSubmission/Solution.lean#L20](https://github.com/deancureton/MovingSofa/blob/a0753860f1d2b4424e059c35e64ad611be71a415/MovingSofaSubmission/Solution.lean#L20); a Lean proof is at [https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L26](https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L26); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L171-L173](https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L171-L173); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L124-L125](https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L124-L125).

> What is the sofa constant?

```lean
theorem sofaConstant_eq : sofaConstant = sofaConstant_eq.answer
```

Category `research solved`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 238](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MovingSofa.lean#L238).

## `MovingSofa.sofaConstant_eq_volume_gerversSofa`

Solved: stated here; a Lean proof is at [https://github.com/deancureton/MovingSofa/blob/a0753860f1d2b4424e059c35e64ad611be71a415/MovingSofaSubmission/Solution.lean#L20](https://github.com/deancureton/MovingSofa/blob/a0753860f1d2b4424e059c35e64ad611be71a415/MovingSofaSubmission/Solution.lean#L20); a Lean proof is at [https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L30](https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L30); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L171-L173](https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L171-L173); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L124-L125](https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L124-L125).

> Gerver's sofa attains the sofa constant, conjectured by [Ge92] and claimed by [Ba24].

```lean
theorem sofaConstant_eq_volume_gerversSofa : sofaConstant = volume gerversSofa
```

Category `research solved`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 248](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MovingSofa.lean#L248).

## `MovingSofa.volume_eq_sofaConstant_iff_congruent_gerversSofa`

Solved: stated here; a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L176-L190](https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L176-L190); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L128-L131](https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L128-L131).

> Gerver's sofa is the unique sofa that attains the sofa constant, up to a rigid motion.
>
> The motion is needed: `horizontalHallway` is $(-\infty, 1] \times [0, 1]$, so a leftward
> translate of any moving sofa is again one, obtained by sliding right and then following the
> original motion. It has the same area, so uniqueness cannot hold on the nose.

```lean
theorem volume_eq_sofaConstant_iff_congruent_gerversSofa (s : Set ℝ²)
    (hs : ∃ m, IsMovingSofa s m) :
    volume s = sofaConstant ↔ ∃ g : E(2), s = g '' gerversSofa
```

Category `research solved`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 262](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MovingSofa.lean#L262).

## `MovingSofa.RomiksSofa.existsUnique_X`

Textbook result, proved here.

> The cubic $x^2 (x + 3) = 8$ has exactly one real root.

```lean
theorem existsUnique_X : ∃! x : ℝ, x ^ 2 * (x + 3) = 8
```

Category `textbook`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 357](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MovingSofa.lean#L357).

## `MovingSofa.RomiksSofa.existsUnique_Y`

Textbook result, proved here.

> The cubic $x (4 x^2 + 3) = 1$ has exactly one real root.

```lean
theorem existsUnique_Y : ∃! x : ℝ, x * (4 * x ^ 2 + 3) = 1
```

Category `textbook`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 368](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MovingSofa.lean#L368).

## `MovingSofa.romiksSofa_area_le_ambidextrousSofaConstant`

Solved: stated here without proof.

> Romik's ambidextrous sofa has area `RomiksSofa.area` [Ro18, Thm. 5], so the ambidextrous sofa
> constant is at least that.

```lean
theorem romiksSofa_area_le_ambidextrousSofaConstant :
    ENNReal.ofReal RomiksSofa.area ≤ ambidextrousSofaConstant
```

Category `research solved`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 396](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MovingSofa.lean#L396).

## `MovingSofa.ambidextrousSofaConstant_eq_romiksSofa_area`

Open: stated without proof.

> Romik's ambidextrous sofa is optimal. Romik derived it from local-optimality considerations and
> proposed it as the solution [Ro18, §1.2, §5]; [Wikipedia] records it as the conjectured optimum.
> Even its local optimality is open [Ro18, §7, Problem 1].

```lean
theorem ambidextrousSofaConstant_eq_romiksSofa_area :
    ambidextrousSofaConstant = ENNReal.ofReal RomiksSofa.area
```

Category `research open`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 406](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MovingSofa.lean#L406).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/MovingSofa.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MovingSofa.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Moving_sofa_problem)
