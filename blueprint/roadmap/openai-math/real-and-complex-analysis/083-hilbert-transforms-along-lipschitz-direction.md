---
declaration: section
origin: cited
lean: OAI.LipschitzHilbert.main, OAI.LipschitzHilbert.uniform_truncation
statement: formalized
proof: formalized
---

# 083. Hilbert transforms along Lipschitz directions

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves a uniform strong $L^{2}$ bound for the planar Hilbert transform along any Lipschitz unit vector field, at integration lengths bounded by an absolute multiple of its reciprocal Lipschitz constant. The estimate is uniform over inner truncations and yields an $L^{2}$-bounded principal-value operator, establishing Stein's weak-type conjecture at this short scale.

## A uniform Hilbert transform estimate for Lipschitz directions

We prove a uniform $L^{2}$ bound for the Hilbert transform along a Lipschitz unit vector field in the plane, with integration restricted to a fixed absolute multiple of the reciprocal Lipschitz seminorm. The bound is uniform in the inner truncation and holds for fields depending on both coordinates. This gives an affirmative answer to Stein's weak-$(2,2)$ conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves uniform $L^2$ bounds for short Hilbert transforms along Lipschitz unit vector fields in the plane, including fields depending on both coordinates. For Lipschitz constant $K>0$, every hard truncation with $0<\varepsilon\le R\le1/(10^6K)$ has one universal $L^2$ bound on Schwartz functions, independent of the inner cutoff.

At a fixed short scale for $1$-Lipschitz fields, the formalization also gives principal-value and weak-$(2,2)$ estimates and bounded extensions to all of $L^2$. These results establish the stated short-scale form of Stein's question.

## Lean: Uniform short Hilbert-transform bounds for Lipschitz directions

```lean
theorem main :
    ∃ a : ℝ, a∈Ioo 0 (1/2) ∧ ∃ C : ℝ≥0, 0<C ∧ ShortHilbertConclusion a C
```

Stated in [LipschitzHilbert.lean, line 63](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LipschitzHilbert.lean#L63). Proved in [lean/OAI/Analysis/LipschitzHilbert/Main.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/LipschitzHilbert/Main.lean#L17).

```lean
theorem uniform_truncation :
    ∃ C : ℝ, 0<C ∧ ∀ K : ℝ≥0, 0<K → ∀ epsilon R : ℝ,
      0<epsilon → epsilon≤R → R≤1/(1000000*(K:ℝ)) →
      ∀ v : Plane → Plane, LipschitzWith K v → (∀ x, ‖v x‖=1) →
      ∀ f : SchwartzMap Plane ℂ,
        eLpNorm (shortTransform v epsilon R f) 2 volume≤ENNReal.ofReal (C*‖f.toLp 2 volume‖)
```

Stated in [LipschitzHilbert.lean, line 68](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LipschitzHilbert.lean#L68). Proved in [lean/OAI/Analysis/LipschitzHilbert/Main.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/LipschitzHilbert/Main.lean#L23).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/083.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/083.md)
