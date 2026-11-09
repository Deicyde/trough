---
declaration: theorem
origin: cited
lean: Erdos189.erdos_189, Erdos189.erdos_189.variants.square, Erdos189.erdos_189.variants.parallelogram
statement: formalized
---

# Erdős Problem 189

> *Reference:* [erdosproblems.com/189](https://www.erdosproblems.com/189)

*Quoted from [FormalConjectures/ErdosProblems/189.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/189.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/189](https://www.erdosproblems.com/189).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos189.erdos_189`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos189.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos189.lean).

> If $\mathbb{R}^2$ is finitely coloured then must there exist some colour class which contains the
> vertices of a rectangle of every area?
>
> Graham, "On Partitions of 𝔼ⁿ", Journal of Combinatorial Theory, Series A 28, 89-91 (1980).
> (See "Concluding Remarks" on page 96.)
>
> Solved (with answer `False`, as formalised below) in:
> Vjekoslav Kovač, "Coloring and density theorems for configurations of a given volume", 2023
> https://arxiv.org/abs/2309.09973
> In fact, Kovač's colouring is even Jordan measurable (the topological boundary of each
> monochromatic region is Lebesgue measurable and has measure zero).
>
> This was formalized in Lean by Alexeev and Kovac using Aristotle.

```lean
theorem erdos_189 :
    ¬ Erdos189For
      (fun a b c d ↦
        line[ℝ, a, b].direction ⟂ line[ℝ, b, c].direction ∧
        line[ℝ, b, c].direction ⟂ line[ℝ, c, d].direction ∧
        line[ℝ, c, d].direction ⟂ line[ℝ, d, a].direction)
      (fun a b c d ↦ dist a b * dist b c)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/189.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/189.lean#L57).

## `Erdos189.erdos_189.variants.square`

Solved: stated here without proof.

> Graham claims this is "easy to see".

```lean
theorem erdos_189.variants.square :
    ¬ Erdos189For
      (fun a b c d ↦
        line[ℝ, a, b].direction ⟂ line[ℝ, b, c].direction ∧
        line[ℝ, b, c].direction ⟂ line[ℝ, c, d].direction ∧
        line[ℝ, c, d].direction ⟂ line[ℝ, d, a].direction ∧
        dist a b = dist b c)
      (fun a b c d ↦ dist a b * dist b c)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/189.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/189.lean#L68).

## `Erdos189.erdos_189.variants.parallelogram`

Open: stated without proof.

> Seems to be open, as of January 2025.

```lean
theorem erdos_189.variants.parallelogram :
    ¬ Erdos189For
      (fun a b c d ↦
        line[ℝ, a, b] ∥ line[ℝ, c, d] ∧
        line[ℝ, a, d] ∥ line[ℝ, b, c])
      (fun a b c d ↦ dist a b * dist b c * (∡ a b c).sin)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/189.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/189.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/189.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/189.lean)
- [erdosproblems.com/189](https://www.erdosproblems.com/189)
