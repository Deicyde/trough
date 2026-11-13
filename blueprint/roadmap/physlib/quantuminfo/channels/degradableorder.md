---
declaration: module
origin: cited
lean: DegradablePreorder
statement: formalized
proof: formalized
---

# The Degradable Order

The module `QuantumInfo.Channels.DegradableOrder`, [QuantumInfo/Channels/DegradableOrder.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/DegradableOrder.lean): 1 declaration, 0 with a docstring.

> We define the "degradable order" on channels, where M ≤ N if N can be degraded to M. This is a
> scoped instance, because there are other reasonable orders on channels.
>
> The degradable order is actually only a preorder, because channels that are degradable to each other
> are not necessarily equal. (For instance, unitary channels are degradable to the identity and vice
> versa.) It can compare channels of different output dimensions, but they must have the same input
> dimension. For this reason the `DegradablePreorder` is parameterized by the channel input type.
>
> One might hope that if this was defined on the quotient type of "channels up to unitary equivalence"
> that it would become an order; but this is not the case. That is, there are channels `A → B` that
> are degradable to each other, but cannot be degraded to each other by unitary operations. For
> instance, let A be the replacement channel that goes to a mixed state, and B be a replacement
> channel that goes to a pure state.
>
> Technical notes: to model "channels of different output types", the preorder is on the Sigma type of
> channels parameterized by their output type. And since the output type needs to be a Fintype and
> DecidableEq, the argument is also a Sigma to bring this along.

**`DegradablePreorder`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/DegradableOrder.lean#L37).

```lean
def DegradablePreorder (dIn : Type*) [Fintype dIn] [DecidableEq dIn] : Preorder
    (Σ dOut : (Σ t, Fintype t × DecidableEq t), let _ := dOut.snd.1; CPTPMap dIn dOut.fst)
```

## Depends on

- [Completely Positive Trace Preserving maps](cptp.md)

## Sources

- [QuantumInfo/Channels/DegradableOrder.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/DegradableOrder.lean)
