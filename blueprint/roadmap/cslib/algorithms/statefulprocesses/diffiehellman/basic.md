---
catalog: module
lean: Cslib.Algorithms.StatefulProcesses.DiffieHellman.shared_secret_eq, Cslib.Algorithms.StatefulProcesses.DiffieHellman.aliceProc, Cslib.Algorithms.StatefulProcesses.DiffieHellman.bobProc, Cslib.Algorithms.StatefulProcesses.DiffieHellman.aliceProc₁, Cslib.Algorithms.StatefulProcesses.DiffieHellman.aliceProc₂, Cslib.Algorithms.StatefulProcesses.DiffieHellman.bobProc₁, Cslib.Algorithms.StatefulProcesses.DiffieHellman.bobProc₂, Cslib.Algorithms.StatefulProcesses.DiffieHellman.net
statement: formalized
proof: formalized
---

# Diffie-Hellman Key Exchange in Stateful Processes (testbed)

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.Basic`, in [Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean), by Fabrizio Montesi.

> This module formalises the Diffie-Hellman key exchange protocol in `StatefulProcesses`.
>
> It is also intended as a simple testbed to measure improvement on how CSLib deals with embedded DSLs
> like Stateful Processes and reasoning on operational semantics.
>
> Current aspects that stand out and could be more ergonomic are:
> 1. The protocol has two obvious symbolic traces, yet proving `net_completeTraces` is cumbersome.
>   Perhaps an API for unique transitions could be partially helpful:
> ```
> def _root_.Cslib.LTS.TrUnique (lts : LTS State Label) (s : State) (μ : Label) (s' : State) :=
>   lts.Tr s μ s' ∧ ∀ μ' s'', lts.Tr s μ' s'' → μ' = μ ∧ s'' = s'
> ```
>   The terms for `aliceProc` and `bobProc` after one and two steps of their executions are provided
>   as reference for this endeavour.
> 2. As a consequence of (1), proving `net_fun_correct` is cumbersome.
>
> ## Implementation notes
>
> The public parameters are a generator `g : ZMod p`, with the modulus `p` left implicit. Each role
> takes only what its participant knows: the public parameters, the identity of its peer, and handles
> to its own local variables.
>
> Private exponents are local variables rather than Lean constants, so they live in the
> participants' stores and never occur in the process terms or in their transition labels. As a
> consequence, correctness statements assume that, in each role, the variable receiving the peer's
> public value differs from the exponent, which the reception would otherwise overwrite.
>
> The key-agreement computation does not require primality or a primitive root; security properties
> would require additional assumptions.

> ## Basics

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.shared_secret_eq` (theorem, [line 55](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L55))

> The two participants compute the same shared key.

```lean
theorem shared_secret_eq (p : ℕ) (g : ZMod p) (a b : ℕ) :
    (g ^ b) ^ a = (g ^ a) ^ b
```

> ## Behaviour

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.aliceProc` (definition, [line 65](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L65))

> Alice's program, the initiator. It sends `g ^ a` to `bob`, receives Bob's public value in
> `peerPub`, and stores the shared key in `key`. The private exponent `a` is a local variable.

```lean
def aliceProc (bob : Pid) (g : ZMod p) (a : L.Var ℕ) (peerPub key : L.Var (ZMod p)) :
    Process Pid L SelLabel ProcName
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.bobProc` (definition, [line 74](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L74))

> Bob's program, the responder. It receives Alice's public value in `peerPub`, sends `g ^ b` to
> `alice`, and stores the shared key in `key`. The private exponent `b` is a local variable.

```lean
def bobProc (alice : Pid) (g : ZMod p) (b : L.Var ℕ) (peerPub key : L.Var (ZMod p)) :
    Process Pid L SelLabel ProcName
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.aliceProc₁` (definition, [line 82](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L82))

> Alice's program after its first communication.

```lean
def aliceProc₁ (bob : Pid) (a : L.Var ℕ) (peerPub key : L.Var (ZMod p)) :
    Process Pid L SelLabel ProcName
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.aliceProc₂` (definition, [line 87](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L87))

> Alice's program after both communications.

```lean
def aliceProc₂ (a : L.Var ℕ) (peerPub key : L.Var (ZMod p)) : Process Pid L SelLabel ProcName
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.bobProc₁` (definition, [line 91](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L91))

> Bob's program after its first communication.

```lean
def bobProc₁ (alice : Pid) (g : ZMod p) (b : L.Var ℕ) (peerPub key : L.Var (ZMod p)) :
    Process Pid L SelLabel ProcName
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.bobProc₂` (definition, [line 96](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L96))

> Bob's program after both communications.

```lean
def bobProc₂ (b : L.Var ℕ) (peerPub key : L.Var (ZMod p)) : Process Pid L SelLabel ProcName
```

> ## The protocol

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.net` (definition, [line 107](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L107))

> The protocol between Alice (`alice`) and Bob (`bob`), whose local signatures are `S alice` and
> `S bob`. Alice's private exponent is in `a`, she receives Bob's public value in `y`, and she stores
> the key in `aliceKey`. Bob's private exponent is in `b`, he receives Alice's public value in `x`,
> and he stores the key in `bobKey`.

```lean
def net (g : ZMod p) (alice bob : Pid) (a : S.Var alice ℕ) (y aliceKey : S.Var alice (ZMod p))
    (b : S.Var bob ℕ) (x bobKey : S.Var bob (ZMod p)) : Network Pid S SelLabel ProcName
```

## Depends on

- [Networks of stateful processes and their semantics](../../../languages/statefulprocesses/network.md)

## Sources

- [Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Algorithms.StatefulProcesses.DiffieHellman.Basic.json)
