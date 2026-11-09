---
declaration: theorem
origin: cited
lean: Erdos1176.erdos_1176
statement: formalized
---

# Erdős Problem 1176

> *Reference:* [erdosproblems.com/1176](https://www.erdosproblems.com/1176)

*Quoted from [FormalConjectures/ErdosProblems/1176.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1176.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1176](https://www.erdosproblems.com/1176).

The file states 1 research or textbook statement: 1 open.

## `Erdos1176.erdos_1176`

Open: stated without proof.

> Let $G$ be a graph with chromatic number $\aleph_1$. Is it true that there is a colouring of the
> edges with $\aleph_1$ many colours such that, in any countable colouring of the vertices, there
> exists a vertex colour containing all edge colours?
>
> A problem of Erdős, Galvin, and Hajnal. The consistency of this was proved by Hajnal and Komjáth.

```lean
theorem erdos_1176 :
    ∀ {V : Type*} (G : SimpleGraph V), G.chromaticCardinal = aleph 1 →
      ∃ (EColor : Type) (_ : mk EColor = aleph 1) (c_edge : G.edgeSet → EColor),
        ∀ (VColor : Type) (_ : mk VColor ≤ aleph 0) (c_vert : V → VColor),
          ∃ (vc : VColor),
            ∀ (ec : EColor), ∃ (u v : V) (h : G.Adj u v),
              c_vert u = vc ∧ c_vert v = vc ∧ c_edge ⟨s(u, v), h⟩ = ec
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1176.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1176.lean#L40).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1176.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1176.lean)
- [erdosproblems.com/1176](https://www.erdosproblems.com/1176)
