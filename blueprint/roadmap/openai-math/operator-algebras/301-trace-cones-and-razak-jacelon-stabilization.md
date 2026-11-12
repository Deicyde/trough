---
declaration: section
origin: cited
lean: OAI.TraceConeClassification.TraceConeEquiv.idealOrderIso_finIdeal, OAI.TraceConeClassification.TraceConeEquiv.idealOrderIso_zeroIdeal, OAI.TraceConeClassification.closed_ideal_weight_exists, OAI.TraceConeClassification.ExtendedTrace.zero_mem_finiteSquareSet, OAI.TraceConeClassification.ExtendedTrace.star_mem_finiteSquareSet, OAI.TraceConeClassification.ExtendedTrace.smul_mem_finiteSquareSet, OAI.TraceConeClassification.ExtendedTrace.add_mem_finiteSquareSet, OAI.TraceConeClassification.ExtendedTrace.mul_mem_finiteSquareSet_left
statement: formalized
proof: formalized
---

# 301. Trace cones and Razak–Jacelon stabilization

1 manuscript and 17 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Classifies separable nuclear complex $C^{∗}$-algebras after tensoring with the Razak–Jacelon algebra and the compact operators, using their full topological cones of extended lower-semicontinuous tracial weights. This answers Robert’s trace-cone question, including algebras with arbitrary ideal structure and both finite and infinite subquotients.

## The trace cone classifies Razak–Jacelon stabilizations

We prove that the canonical topological cone of all extended lower-semicontinuous tracial weights determines a separable nuclear $C^{∗}$-algebra after tensoring with the Razak–Jacelon algebra and the compact operators, answering Robert's trace-cone classification question positively. The isomorphism realizes the prescribed cone map, with arbitrary ideal structure and without a density assumption on the finite domains of the weights.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The paper classifies separable nuclear complex $C^*$-algebras after tensoring with the Razak–Jacelon algebra and the compact operators, using their cones of extended lower-semicontinuous traces. The linked formalization proves the supporting ideal-transport result from Section 2: a trace-cone equivalence induces an order isomorphism of closed two-sided ideals, carrying the ideals determined by finiteness and vanishing of each trace to those of its image. Here a trace-cone equivalence preserves addition, zero, positive scalar multiplication, and canonical convergence in both directions. The finite ideal is the norm closure of $\{x : \tau(x^*x)<\infty\}$; the zero ideal is characterized on positive elements by $\tau(a)=0$.

For each closed ideal $I$, it also constructs the trace that is zero on positive elements of $I$ and infinite elsewhere. These traces are exactly the additive idempotents, meaning $\tau+\tau=\tau$, and their addition recovers ideal inclusion.

The construction includes proofs of the required ideal and closure properties of the finite domain. It also proves lower semicontinuity of the support weight, which is zero where a given trace vanishes and infinite elsewhere.

The paper's main conclusion is an actual isomorphism $A\otimes\mathcal W\otimes\mathcal K\cong B\otimes\mathcal W\otimes\mathcal K$ realizing the trace-cone data. This comparison does not establish that conclusion. Existence of the stabilization models, norm uniqueness, and final intertwining are also outside it.

## Lean: Transport of trace ideals and their additive-idempotent description

Stated in [TraceIdealTransportSupport.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TraceIdealTransportSupport.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem idealOrderIso_finIdeal (τ : ExtendedTrace A) :
    F.idealOrderIso τ.finIdeal = (F.toEquiv τ).finIdeal
```

Proved in [lean/OAI/Analysis/TraceCone/IdealTransport.lean, line 400](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/IdealTransport.lean#L400).

```lean
theorem idealOrderIso_zeroIdeal (τ : ExtendedTrace A) :
    F.idealOrderIso τ.zeroIdeal = (F.toEquiv τ).zeroIdeal
```

Proved in [lean/OAI/Analysis/TraceCone/IdealTransport.lean, line 411](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/IdealTransport.lean#L411).

```lean
theorem closed_ideal_weight_exists
    (I : NonUnitalStarSubalgebra ℂ A) (hI : IsClosed (I : Set A))
    (hleft : ∀ (x y : A), y ∈ I → x * y ∈ I)
    (hright : ∀ (x y : A), x ∈ I → x * y ∈ I) :
    ∃ τ : ExtendedTrace A, ∀ a : Positive A, τ a = if a.1 ∈ I then 0 else ∞
```

Proved in [lean/OAI/Analysis/TraceCone/FiniteIdeal.lean, line 106](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/FiniteIdeal.lean#L106).

```lean
lemma zero_mem_finiteSquareSet : (0 : A) ∈ τ.finiteSquareSet
```

Proved in [lean/OAI/Analysis/TraceCone/FiniteIdeal.lean, line 174](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/FiniteIdeal.lean#L174).

```lean
lemma star_mem_finiteSquareSet {x : A} (hx : x ∈ τ.finiteSquareSet) :
    star x ∈ τ.finiteSquareSet
```

Proved in [lean/OAI/Analysis/TraceCone/FiniteIdeal.lean, line 178](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/FiniteIdeal.lean#L178).

```lean
lemma smul_mem_finiteSquareSet (c : ℂ) {x : A} (hx : x ∈ τ.finiteSquareSet) :
    c • x ∈ τ.finiteSquareSet
```

Proved in [lean/OAI/Analysis/TraceCone/FiniteIdeal.lean, line 187](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/FiniteIdeal.lean#L187).

```lean
lemma add_mem_finiteSquareSet {x y : A}
    (hx : x ∈ τ.finiteSquareSet) (hy : y ∈ τ.finiteSquareSet) :
    x + y ∈ τ.finiteSquareSet
```

Proved in [lean/OAI/Analysis/TraceCone/FiniteIdeal.lean, line 202](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/FiniteIdeal.lean#L202).

```lean
lemma mul_mem_finiteSquareSet_left (x : A) {y : A} (hy : y ∈ τ.finiteSquareSet) :
    x * y ∈ τ.finiteSquareSet
```

Proved in [lean/OAI/Analysis/TraceCone/FiniteIdeal.lean, line 218](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/FiniteIdeal.lean#L218).

```lean
lemma isClosed_finiteIdeal : IsClosed (τ.finiteIdeal : Set A)
```

Proved in [lean/OAI/Analysis/TraceCone/FiniteIdeal.lean, line 246](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/FiniteIdeal.lean#L246).

```lean
lemma mul_mem_finiteIdeal_left (x : A) {y : A} (hy : y ∈ τ.finiteIdeal) :
    x * y ∈ τ.finiteIdeal
```

Proved in [lean/OAI/Analysis/TraceCone/FiniteIdeal.lean, line 249](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/FiniteIdeal.lean#L249).

```lean
lemma mul_mem_finiteIdeal_right {x : A} (hx : x ∈ τ.finiteIdeal) (y : A) :
    x * y ∈ τ.finiteIdeal
```

Proved in [lean/OAI/Analysis/TraceCone/FiniteIdeal.lean, line 256](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/FiniteIdeal.lean#L256).

```lean
lemma lowerSemicontinuous_supportWeight (τ : ExtendedTrace A) :
    LowerSemicontinuous (fun a : Positive A => if τ a = 0 then (0 : ℝ≥0∞) else ∞)
```

Proved in [lean/OAI/Analysis/TraceCone/IdealTransport.lean, line 280](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/IdealTransport.lean#L280).

```lean
theorem weight_idempotent (I : ClosedIdeal A) : I.weight.add I.weight = I.weight
```

Proved in [lean/OAI/Analysis/TraceCone/IdealTransport.lean, line 83](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/IdealTransport.lean#L83).

```lean
theorem finiteIdeal_weight (I : ClosedIdeal A) : I.weight.finiteIdeal = I.1
```

Proved in [lean/OAI/Analysis/TraceCone/IdealTransport.lean, line 89](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/IdealTransport.lean#L89).

```lean
theorem le_iff_add_weight (I J : ClosedIdeal A) :
    I ≤ J ↔ I.weight.add J.weight = I.weight
```

Proved in [lean/OAI/Analysis/TraceCone/IdealTransport.lean, line 108](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/IdealTransport.lean#L108).

```lean
theorem idempotent_eq_weight {τ : ExtendedTrace A} (hτ : τ.add τ = τ) :
    τ.finIdeal.weight = τ
```

Proved in [lean/OAI/Analysis/TraceCone/IdealTransport.lean, line 151](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/IdealTransport.lean#L151).

```lean
lemma closedIdealEquivOfAdditive_weight (e : ExtendedTrace A ≃ ExtendedTrace B)
    (he : ∀ τ σ, e (τ.add σ) = (e τ).add (e σ)) (I : ClosedIdeal A) :
    (closedIdealEquivOfAdditive e he I).weight = e I.weight
```

Proved in [lean/OAI/Analysis/TraceCone/IdealTransport.lean, line 210](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TraceCone/IdealTransport.lean#L210).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/301.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/301.md)
