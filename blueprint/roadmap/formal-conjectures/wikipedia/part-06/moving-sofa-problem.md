---
declaration: theorem
origin: cited
lean: MovingSofa.GerversSofa.ABφθSpec.existsUnique, MovingSofa.isMovingSofa_gerversSofa, MovingSofa.sofaConstant_eq, MovingSofa.sofaConstant_eq_volume_gerversSofa, MovingSofa.volume_eq_sofaConstant_iff_congruent_gerversSofa
statement: formalized
---

# Moving Sofa Problem

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Moving_sofa_problem)
> - [Ge92] Gerver, J. L., _On moving a sofa around a corner_. Geometriae Dedicata 42.3 (1992): 267-283.
> - [Ro18] Romik, D. _Differential equations and exact solutions in the moving sofa problem_. Experimental mathematics 27.3 (2018): 316-330.
> - [Ba24] Baek, J. _Optimality of Gerver's Sofa_. arXiv preprint arXiv:2411.19826 (2024).

*Quoted from [FormalConjectures/Wikipedia/MovingSofa.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/MovingSofa.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 4 solved and 1 textbook result. It also has 3 test statements, counted here but not shown.

## `MovingSofa.GerversSofa.ABφθSpec.existsUnique`

Textbook result, stated without proof. A Lean proof is at [https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Defs.lean#L173](https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Defs.lean#L173); a Lean proof is at [https://github.com/dawidmtrela-dotcom/GerverSofaLean/blob/v1.0.0/GerverSofa/KernelOnly/PartE/E24KC6KernelFinalClosure.lean](https://github.com/dawidmtrela-dotcom/GerverSofaLean/blob/v1.0.0/GerverSofa/KernelOnly/PartE/E24KC6KernelFinalClosure.lean).

> There exist unique constants $A$, $B$, $\varphi$, and $\theta$ satisfying the spec.

```lean
theorem ABφθSpec.existsUnique : ∃! ABφθ : ℝ × ℝ × ℝ × ℝ,
    ABφθSpec ABφθ.1 ABφθ.2.1 ABφθ.2.2.1 ABφθ.2.2.2
```

Category `textbook`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 164](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/MovingSofa.lean#L164).

## `MovingSofa.isMovingSofa_gerversSofa`

Solved: stated here; a Lean proof is at [https://github.com/dawidmtrela-dotcom/GerverSofaLean/releases/tag/v1.1.0](https://github.com/dawidmtrela-dotcom/GerverSofaLean/releases/tag/v1.1.0); a Lean proof is at [https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L20](https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L20); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L161-L168](https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L161-L168); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L120-L121](https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L120-L121).

> Gerver's concrete sofa admits a valid hallway motion.

```lean
theorem isMovingSofa_gerversSofa : ∃ m, IsMovingSofa gerversSofa m
```

Category `research solved`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 212](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/MovingSofa.lean#L212).

## `MovingSofa.sofaConstant_eq`

Solved: stated here; a Lean proof is at [https://github.com/deancureton/MovingSofa/blob/a0753860f1d2b4424e059c35e64ad611be71a415/MovingSofaSubmission/Solution.lean#L20](https://github.com/deancureton/MovingSofa/blob/a0753860f1d2b4424e059c35e64ad611be71a415/MovingSofaSubmission/Solution.lean#L20); a Lean proof is at [https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L26](https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L26); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L171-L173](https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L171-L173); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L124-L125](https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L124-L125).

> What is the sofa constant?

```lean
theorem sofaConstant_eq : sofaConstant = sofaConstant_eq.answer
```

Category `research solved`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 238](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/MovingSofa.lean#L238).

## `MovingSofa.sofaConstant_eq_volume_gerversSofa`

Solved: stated here; a Lean proof is at [https://github.com/deancureton/MovingSofa/blob/a0753860f1d2b4424e059c35e64ad611be71a415/MovingSofaSubmission/Solution.lean#L20](https://github.com/deancureton/MovingSofa/blob/a0753860f1d2b4424e059c35e64ad611be71a415/MovingSofaSubmission/Solution.lean#L20); a Lean proof is at [https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L30](https://github.com/RuifengCao/sofa-formal/blob/838baca722560f30ea8e60b8c711b20147626175/SofaSubmission/Solution.lean#L30); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L171-L173](https://github.com/vltanh/lean4-moving-sofa/blob/16653ae81e0e4f52a362bafae2ad3440100ad065/Solution.lean#L171-L173); a Lean proof is at [https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L124-L125](https://github.com/vltanh/lean4-moving-sofa/blob/0addd87e5a0a4550ab8a60019180f012167fa24f/Solution.lean#L124-L125).

> Gerver's sofa attains the sofa constant, conjectured by [Ge92] and claimed by [Ba24].

```lean
theorem sofaConstant_eq_volume_gerversSofa : sofaConstant = volume gerversSofa
```

Category `research solved`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 248](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/MovingSofa.lean#L248).

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

Category `research solved`; AMS [49 Calculus of variations and optimal control; optimization](../../by-subject/part-02/49-calculus-of-variations-and-optimal-control-optim/README.md). Declared in [FormalConjectures/Wikipedia/MovingSofa.lean, line 262](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/MovingSofa.lean#L262).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/MovingSofa.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/MovingSofa.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Moving_sofa_problem)
