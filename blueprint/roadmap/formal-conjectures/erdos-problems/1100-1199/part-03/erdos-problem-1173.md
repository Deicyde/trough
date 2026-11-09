---
declaration: theorem
origin: cited
lean: Erdos1173.erdos_1173, Erdos1173.erdos_1173.variants.free_set_mono, Erdos1173.erdos_1173.variants.image_lt_aleph_succ
statement: formalized
---

# Erdős Problem 1173

> *Reference:* [erdosproblems.com/1173](https://www.erdosproblems.com/1173)

*Quoted from [FormalConjectures/ErdosProblems/1173.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1173.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1173](https://www.erdosproblems.com/1173).

The file states 3 research or textbook statements: 1 open and 2 textbook results. It also has 4 test statements, counted here but not shown.

## `Erdos1173.erdos_1173`

Open: stated without proof.

> **Erdős–Hajnal Problem 1173** [EH74]. Assume GCH. Let
> $f : \omega_{\omega+1} \to [\omega_{\omega+1}]^{\leq \aleph_\omega}$
> be a set mapping such that $|f(\alpha) \cap f(\beta)| < \aleph_\omega$ for all
> $\alpha \neq \beta$. Does there exist a free set of cardinality $\aleph_{\omega+1}$?

```lean
theorem erdos_1173 :
    GCH →
    ∀ f : (ω_ (ω + 1)).ToType → Set (ω_ (ω + 1)).ToType,
      IsSetMapping f →
      ∃ Y : Set (ω_ (ω + 1)).ToType, IsFreeSet f Y ∧ #Y = ℵ_ (ω + 1)
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/1173.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1173.lean#L55).

## `Erdos1173.erdos_1173.variants.free_set_mono`

Textbook result, proved here.

> Free sets are downward-closed under inclusion.

```lean
theorem erdos_1173.variants.free_set_mono
    (f : (ω_ (ω + 1)).ToType → Set (ω_ (ω + 1)).ToType)
    {Y Z : Set (ω_ (ω + 1)).ToType}
    (hYZ : Z ⊆ Y) (hY : IsFreeSet f Y) : IsFreeSet f Z
```

Category `textbook`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/1173.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1173.lean#L94).

## `Erdos1173.erdos_1173.variants.image_lt_aleph_succ`

Textbook result, proved here.

> Under `IsSetMapping f`, each image has cardinality `< ℵ_{ω+1}`.

```lean
theorem erdos_1173.variants.image_lt_aleph_succ
    (f : (ω_ (ω + 1)).ToType → Set (ω_ (ω + 1)).ToType)
    (hf : IsSetMapping f)
    (α : (ω_ (ω + 1)).ToType) :
    #(f α) < ℵ_ (ω + 1)
```

Category `textbook`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/1173.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1173.lean#L103).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1173.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1173.lean)
- [erdosproblems.com/1173](https://www.erdosproblems.com/1173)
