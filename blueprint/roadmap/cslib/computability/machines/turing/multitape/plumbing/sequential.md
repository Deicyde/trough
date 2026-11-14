---
catalog: module
lean: Turing.MultiTapeTM.seq, Turing.MultiTapeTM.exists_runPath_seq, Turing.MultiTapeTM.transformsTapes_seq
statement: formalized
proof: formalized
---

# Sequential composition of machines on shared tapes

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.Sequential`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Sequential.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Sequential.lean), by Christian Reitwiessner, Samuel Schlesinger.

> `seq tm₀ tm₁` behaves like `tm₀` until `tm₀` would halt, at which point it continues as `tm₁`,
> started in its initial state on the tapes as `tm₀` left them. The state space is
> `State₀ ⊕ State₁`, and the *halting transition* of the first phase is mapped to the initial state
> of the second, so the handoff costs no extra step.
>
> At the specification level this is `transformsTapes_seq`: transformations compose, with the time
> and space bounds adding. The postcondition of `TransformsTapes` is what makes the proof direct:
> the first machine halts in a full `wordsCfg`, which is exactly a starting configuration for the
> second.
>
> ## Main results
>
> * `Turing.MultiTapeTM.seq`: the composed machine.
> * `Turing.MultiTapeTM.exists_runPath_seq`: run paths compose, and the composed path visits only
>   cells that the two paths visit.
> * `Turing.MultiTapeTM.transformsTapes_seq`: transformations compose, bounds adding.

`Turing.MultiTapeTM.seq` (abbreviation, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Sequential.lean#L41))

> The sequential composition of `tm₀` and `tm₁`: it behaves like `tm₀` until `tm₀` would halt,
> at which point it switches to the initial state of `tm₁` and behaves like `tm₁`. The switch is
> folded into the halting transition of `tm₀`, so it costs no step.

```lean
noncomputable abbrev seq (tm₀ : MultiTapeTM k Symbol State₀) (tm₁ : MultiTapeTM k Symbol State₁) :
    MultiTapeTM k Symbol (State₀ ⊕ State₁)
```

`Turing.MultiTapeTM.exists_runPath_seq` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Sequential.lean#L51))

> **Sequential composition of runs.** A run path of `tm₀` to a halted configuration and a run path
> of `tm₁` started where `tm₀` halted combine into a run path of `seq`: the first path up to its first
> halted configuration, followed by the second. It takes at most as many steps as the two paths
> together, and visits only cells that they visit.

```lean
theorem exists_runPath_seq {p₀ : tm₀.RunPath input} (h₀ : p₀.last.Halted)
    {p₁ : tm₁.RunPath input} (h₁ : p₁.head = p₀.last.withState (some tm₁.q₀)) :
    ∃ p : (tm₀.seq tm₁).RunPath input, p.head = p₀.head.mapState (handOver tm₁.q₀) ∧
      p.last = p₁.last.mapState (Option.map .inr) ∧ p.length ≤ p₀.length + p₁.length ∧
      ∀ i, p.visitedByTapeHead i ⊆ p₀.visitedByTapeHead i ∪ p₁.visitedByTapeHead i
```

`Turing.MultiTapeTM.transformsTapes_seq` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Sequential.lean#L72))

> **Sequential composition of transformations.** If the postcondition of the first
> transformation implies the precondition of the second, the composed machine performs the two
> transformations one after the other, with the time and space bounds adding and the emitted words
> concatenating.

```lean
theorem transformsTapes_seq
    {P₀ P₁ : (input : List Symbol) → (Fin k → List Symbol) → Prop}
    {Q₀ Q₁ : (input : List Symbol) → (Fin k → List Symbol) → (Fin k → List Symbol) →
      List Symbol → Prop}
    {t₀ s₀ t₁ s₁ : ℕ}
    (h₀ : TransformsTapes tm₀ P₀ Q₀ t₀ s₀) (h₁ : TransformsTapes tm₁ P₁ Q₁ t₁ s₁)
    (hmid : ∀ input ws ws' e, P₀ input ws → Q₀ input ws ws' e → P₁ input ws') :
    TransformsTapes (tm₀.seq tm₁) P₀
      (fun input ws ws'' e => ∃ ws' e₀ e₁, Q₀ input ws ws' e₀ ∧ Q₁ input ws' ws'' e₁ ∧
        e = e₀ ++ e₁)
      (t₀ + t₁) (s₀ + s₁)
```

## Depends on

- [Machines as transformers of tape words](transformstapes.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Sequential.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/Sequential.lean)
