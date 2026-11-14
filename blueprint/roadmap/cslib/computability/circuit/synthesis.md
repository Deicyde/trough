---
catalog: module
lean: Cslib.Circuits.inputs, Cslib.Circuits.available, Cslib.Circuits.mem_available, Cslib.Circuits.inputs_subset_available, Cslib.Circuits.Synthesis, Cslib.Circuits.Synthesis.of_subset, Cslib.Circuits.Synthesis.of_mem, Cslib.Circuits.Synthesis.mono, Cslib.Circuits.Synthesis.comp, Cslib.Circuits.Synthesis.trans, Cslib.Circuits.Synthesis.union, Cslib.Circuits.Synthesis.gate, Cslib.Circuits.Synthesis.biUnion, Cslib.Circuits.Synthesis.iUnion, Cslib.Circuits.Synthesis.family, Cslib.Circuits.Synthesis.gate_of_syntheses, Cslib.Circuits.Synthesis.nullary, Cslib.Circuits.Synthesis.unary, Cslib.Circuits.Synthesis.binary, Cslib.Circuits.Synthesis.combine, Cslib.Circuits.Synthesis.foldr, Cslib.Circuits.Synthesis.finset_fold, Cslib.Circuits.Synthesis.exists_circuit_outputs, Cslib.Circuits.Synthesis.exists_circuit
statement: formalized
proof: formalized
---

# Simultaneous circuit synthesis

`Cslib.Computability.Circuit.Synthesis`, in [Cslib/Computability/Circuit/Synthesis.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean), by Samuel Schlesinger.

> `Synthesis I sources targets cost` bounds the number of additional gates needed to compute
> `targets` from `sources` under an interpretation `I`. Every function already available in the
> starting program remains available, so successive constructions can share intermediate results.
> The signature and its carrier are arbitrary; neither needs to be finite or decidable.
>
> The core rules compose bounds, combine finite families, and apply operations of the signature,
> either to functions that are already available or to functions synthesized in turn. Composition
> keeps everything built along the way available to later steps. The fold rules accept a bound
> for combining two arguments, which may itself use several gates.
> `Synthesis.exists_circuit_outputs` selects any tuple of outputs without adding gates;
> `Synthesis.exists_circuit` specializes this to a single output.

`Cslib.Circuits.inputs` (definition, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L40))

> The coordinate projections supplied by the circuit's inputs.

```lean
def inputs (n : ℕ) : Set ((Fin n → U) → U)
```

`Cslib.Circuits.available` (definition, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L44))

> The functions computed by the wires of `p`, whether input wires or internal
> gates.

```lean
def available (I : Interpretation σ U) {g : ℕ} (p : Program σ n g) : Set ((Fin n → U) → U)
```

`Cslib.Circuits.mem_available` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L48))

> A function is available exactly when some wire computes it pointwise.

```lean
theorem mem_available {g : ℕ} {p : Program σ n g} {f : (Fin n → U) → U} :
    f ∈ available I p ↔ ∃ w, ∀ x, p.trace I x w = f x
```

`Cslib.Circuits.inputs_subset_available` (theorem, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L53))

> The input projections are available in every program.

```lean
theorem inputs_subset_available {g : ℕ} (p : Program σ n g) :
    inputs n ⊆ available I p
```

`Cslib.Circuits.Synthesis` (definition, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L70))

> `Synthesis I sources targets cost` says that `targets` can be computed from `sources`
> using at most `cost` additional gates, without losing anything already computed.
>
> Precisely: for every program `p₁` on whose wires every function in `sources` is available,
> there is a program `p₂` such that
> * `p₂` has at most `cost` more gates than `p₁`,
> * every function available in `p₁` is still available in `p₂`, and
> * every function in `targets` is available in `p₂`.
>
> Quantifying over an arbitrary starting program, rather than the empty one, is what lets
> constructions share intermediate results: `Synthesis.comp` adds budgets because the second
> construction may reuse wires built by the first.

```lean
def Synthesis (I : Interpretation σ U) (sources targets : Set ((Fin n → U) → U))
    (cost : ℕ) : Prop
```

`Cslib.Circuits.Synthesis.of_subset` (theorem, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L81))

> Available functions require no additional gates.

```lean
theorem of_subset (h : t ⊆ s) : Synthesis I s t 0
```

`Cslib.Circuits.Synthesis.of_mem` (theorem, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L85))

> An available function requires no additional gates.

```lean
theorem of_mem (hf : f ∈ s) : Synthesis I s {f} 0
```

`Cslib.Circuits.Synthesis.mono` (theorem, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L89))

> Enlarge the source family, narrow the target family, or increase the budget.

```lean
theorem mono (h : Synthesis I s t a) {s' t' : Set ((Fin n → U) → U)}
    (hs : s ⊆ s') (ht : t' ⊆ t) (hab : a ≤ b) : Synthesis I s' t' b
```

`Cslib.Circuits.Synthesis.comp` (theorem, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L97))

> Successive constructions add their gate budgets. The second construction may use the
> targets of the first, and both target families remain available.

```lean
theorem comp (h : Synthesis I s t a) (h' : Synthesis I (s ∪ t) t₁ b) :
    Synthesis I s (t ∪ t₁) (a + b)
```

`Cslib.Circuits.Synthesis.trans` (theorem, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L105))

> Successive constructions, keeping only the final targets.

```lean
theorem trans (h : Synthesis I s t a) (h' : Synthesis I (s ∪ t) t₁ b) :
    Synthesis I s t₁ (a + b)
```

`Cslib.Circuits.Synthesis.union` (theorem, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L110))

> Combine two target families, preserving the first while constructing the second.

```lean
theorem union (h : Synthesis I s t a) (h' : Synthesis I s t₁ b) :
    Synthesis I s (t ∪ t₁) (a + b)
```

`Cslib.Circuits.Synthesis.gate` (theorem, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L115))

> Synthesize an operation whose arguments are already available.

```lean
theorem gate (op : σ.Op) (args : Fin (σ.Arity op) → (Fin n → U) → U)
    (hargs : ∀ i, args i ∈ s) :
    Synthesis I s {fun x => I op (fun i => args i x)} 1
```

`Cslib.Circuits.Synthesis.biUnion` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L132))

> Combine a finite family of target sets, retaining all earlier results.

```lean
theorem biUnion (indices : Finset ι) (targets : ι → Set ((Fin n → U) → U))
    (cost : ι → ℕ) (h : ∀ i ∈ indices, Synthesis I s (targets i) (cost i)) :
    Synthesis I s (⋃ i ∈ indices, targets i) (∑ i ∈ indices, cost i)
```

`Cslib.Circuits.Synthesis.iUnion` (theorem, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L143))

> Combine target sets indexed by a finite type.

```lean
theorem iUnion [Fintype ι] (targets : ι → Set ((Fin n → U) → U)) (cost : ι → ℕ)
    (h : ∀ i, Synthesis I s (targets i) (cost i)) :
    Synthesis I s (⋃ i, targets i) (∑ i, cost i)
```

`Cslib.Circuits.Synthesis.family` (theorem, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L149))

> Simultaneously synthesize an indexed finite family of functions.

```lean
theorem family [Fintype ι] (f : ι → (Fin n → U) → U) (cost : ι → ℕ)
    (h : ∀ i, Synthesis I s {f i} (cost i)) :
    Synthesis I s (Set.range f) (∑ i, cost i)
```

`Cslib.Circuits.Synthesis.gate_of_syntheses` (theorem, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L155))

> Synthesize every argument, then apply an operation with one further gate.

```lean
theorem gate_of_syntheses (op : σ.Op) (args : Fin (σ.Arity op) → (Fin n → U) → U)
    (cost : Fin (σ.Arity op) → ℕ) (h : ∀ i, Synthesis I s {args i} (cost i)) :
    Synthesis I s {fun x => I op (fun i => args i x)} ((∑ i, cost i) + 1)
```

`Cslib.Circuits.Synthesis.nullary` (theorem, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L161))

> A nullary operation supplies its interpreted constant with one gate.

```lean
theorem nullary (op : σ.Op) (arity : σ.Arity op = 0) :
    Synthesis I s {fun _ => I op (fun i => Fin.elim0 (Fin.cast arity i))} 1
```

`Cslib.Circuits.Synthesis.unary` (theorem, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L167))

> Feed a synthesized function to every argument of an operation, using one further gate.
> In particular, this applies a unary operation.

```lean
theorem unary (h : Synthesis I s {f} a) (op : σ.Op) :
    Synthesis I s {fun x => I op (fun _ => f x)} (a + 1)
```

`Cslib.Circuits.Synthesis.binary` (theorem, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L173))

> Feed `f` to argument zero and `g` to the remaining arguments, using one further gate.
> For a binary operation, these are its two arguments.

```lean
theorem binary (hf : Synthesis I s {f} a) (hg : Synthesis I s {g} b) (op : σ.Op) :
    Synthesis I s {fun x => I op (fun i => if i.val = 0 then f x else g x)}
      (a + b + 1)
```

`Cslib.Circuits.Synthesis.combine` (theorem, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L181))

> Apply a synthesis bound to two previously synthesized arguments. The combining
> construction can use several gates and can reuse either argument.

```lean
theorem combine {result : (Fin n → U) → U} {c : ℕ}
    (hf : Synthesis I s {f} a) (hg : Synthesis I s {g} b)
    (h : Synthesis I {f, g} {result} c) : Synthesis I s {result} (a + b + c)
```

`Cslib.Circuits.Synthesis.foldr` (theorem, [line 191](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L191))

> Fold an ordered list of synthesized functions. No algebraic laws are needed for the
> combining operation. The seed and the combining construction have their own gate budgets.

```lean
theorem foldr (op : U → U → U) (combineCost : ℕ)
    (hop : ∀ f g : (Fin n → U) → U,
      Synthesis I {f, g} {fun x => op (f x) (g x)} combineCost)
    (indices : List ι) {f : ι → (Fin n → U) → U} {cost : ι → ℕ}
    {seed : (Fin n → U) → U} (hseed : Synthesis I s {seed} a)
    (h : ∀ i ∈ indices, Synthesis I s {f i} (cost i)) :
    Synthesis I s {fun x => indices.foldr (fun i acc => op (f i x) acc) (seed x)}
      ((indices.map fun i => cost i + combineCost).sum + a)
```

`Cslib.Circuits.Synthesis.finset_fold` (theorem, [line 209](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L209))

> Fold a finite set of synthesized functions with a commutative associative operation.
> The seed need not be an identity or a constant, and the combining construction may use
> several gates.

```lean
theorem finset_fold (op : U → U → U) [Std.Commutative op] [Std.Associative op]
    (combineCost : ℕ) (hop : ∀ f g : (Fin n → U) → U,
      Synthesis I {f, g} {fun x => op (f x) (g x)} combineCost)
    (indices : Finset ι) {f : ι → (Fin n → U) → U} {cost : ι → ℕ}
    {seed : (Fin n → U) → U} (hseed : Synthesis I s {seed} a)
    (h : ∀ i ∈ indices, Synthesis I s {f i} (cost i)) :
    Synthesis I s {fun x => indices.fold op (seed x) (fun i => f i x)}
      ((∑ i ∈ indices, (cost i + combineCost)) + a)
```

`Cslib.Circuits.Synthesis.exists_circuit_outputs` (theorem, [line 228](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L228))

> Select a tuple of outputs from a synthesis bound. Selecting outputs, including repeated
> outputs or none at all, requires no additional gates.

```lean
theorem exists_circuit_outputs {m cost : ℕ} {f : Fin m → (Fin n → U) → U}
    (h : Synthesis I (inputs n) (Set.range f) cost) :
    ∃ c : Circuit σ n m, c.Computes I (fun x j => f j x) ∧ c.size ≤ cost
```

`Cslib.Circuits.Synthesis.exists_circuit` (theorem, [line 236](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean#L236))

> Extract a single-output circuit from a synthesis bound on the input projections.

```lean
theorem exists_circuit {cost : ℕ} (h : Synthesis I (inputs n) {f} cost) :
    ∃ c : Circuit σ n 1, c.Computes I (single f) ∧ c.size ≤ cost
```

## Depends on

- [Circuits](basic.md)

## Sources

- [Cslib/Computability/Circuit/Synthesis.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Synthesis.lean)
