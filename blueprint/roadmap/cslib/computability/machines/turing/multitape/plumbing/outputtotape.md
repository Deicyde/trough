---
catalog: module
lean: Turing.MultiTapeTM.outputToTape, Turing.MultiTapeTM.outCfg, Turing.MultiTapeTM.outCfg_workTapes_last, Turing.MultiTapeTM.outCfg_workTapes_castSucc, Turing.MultiTapeTM.outCfg_workTapePos_last, Turing.MultiTapeTM.outCfg_workTapePos_castSucc, Turing.MultiTapeTM.outCfg_workTapeSymbols_castSucc, Turing.MultiTapeTM.outCfgHom, Turing.MultiTapeTM.initCfg_outputToTape, Turing.MultiTapeTM.space_map_outCfgHom_le
statement: formalized
proof: formalized
---

# Redirecting the output to a work tape

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.OutputToTape`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean), by Christian Reitwiessner, Samuel Schlesinger.

> `outputToTape tm` behaves like `tm`, except that whatever `tm` would append to the write-only
> output tape is written on a fresh work tape instead, whose head always stands at the write
> frontier.
>
> Since the output is append-only, the frontier position is a *function of the configuration* —
> the length of the output so far — so the redirected machine mirrors the original through the
> configuration map `outCfg`, a homomorphism of step relations (`outCfgHom`), so each run path of `tm`
> maps to a run path of the redirected machine.

`Turing.MultiTapeTM.outputToTape` (definition, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean#L31))

> `tm`, with its output writes redirected onto a fresh last work tape, whose head always stands
> at the write frontier.

```lean
public noncomputable def outputToTape (tm : MultiTapeTM k Symbol State) :
    MultiTapeTM (k + 1) Symbol State
```

`Turing.MultiTapeTM.outCfg` (definition, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean#L46))

> A configuration of `tm`, as the redirected machine sees it: the output so far sits on the
> last work tape with the head at its end, and the real output is empty.

```lean
public def outCfg (c : Cfg k Symbol State input) :
    Cfg (k + 1) Symbol State input
```

`Turing.MultiTapeTM.outCfg_workTapes_last` (lemma, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean#L54))

```lean
public lemma outCfg_workTapes_last (c : Cfg k Symbol State input) :
    (outCfg c).workTapes (Fin.last k) = tapeOfList c.output
```

`Turing.MultiTapeTM.outCfg_workTapes_castSucc` (lemma, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean#L59))

```lean
public lemma outCfg_workTapes_castSucc (c : Cfg k Symbol State input) (j : Fin k) :
    (outCfg c).workTapes j.castSucc = c.workTapes j
```

`Turing.MultiTapeTM.outCfg_workTapePos_last` (lemma, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean#L64))

```lean
public lemma outCfg_workTapePos_last (c : Cfg k Symbol State input) :
    (outCfg c).workTapePos (Fin.last k) = (c.output.length : ℤ)
```

`Turing.MultiTapeTM.outCfg_workTapePos_castSucc` (lemma, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean#L69))

```lean
public lemma outCfg_workTapePos_castSucc (c : Cfg k Symbol State input) (j : Fin k) :
    (outCfg c).workTapePos j.castSucc = c.workTapePos j
```

`Turing.MultiTapeTM.outCfg_workTapeSymbols_castSucc` (lemma, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean#L74))

```lean
public lemma outCfg_workTapeSymbols_castSucc (c : Cfg k Symbol State input) (j : Fin k) :
    (outCfg c).workTapeSymbols j.castSucc = c.workTapeSymbols j
```

`Turing.MultiTapeTM.outCfgHom` (definition, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean#L80))

> The redirection preserves steps, so it maps run paths of `tm` to run paths of the redirected
> machine.

```lean
public noncomputable def outCfgHom (tm : MultiTapeTM k Symbol State) :
    (tm.stepRel input).Hom (tm.outputToTape.stepRel input)
```

`Turing.MultiTapeTM.initCfg_outputToTape` (lemma, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean#L91))

> The initial configuration of the redirected machine is the original's through `outCfg`.

```lean
public lemma initCfg_outputToTape (tm : MultiTapeTM k Symbol State) (input : List Symbol) :
    tm.outputToTape.initCfg input = outCfg (tm.initCfg input)
```

`Turing.MultiTapeTM.space_map_outCfgHom_le` (lemma, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean#L99))

> **Space of the output-redirected path.** The `k` inner tapes visit exactly what the original
> path visits, and the frontier head only walks up to the final length of the output, so the
> redirection costs at most the final output length plus one.

```lean
public lemma space_map_outCfgHom_le (tm : MultiTapeTM k Symbol State) (p : tm.RunPath input) :
    (p.map (outCfgHom tm)).space ≤ p.space + (p.last.output.length + 1)
```

## Depends on

- [Deterministic Multi-Tape Turing Machines](../deterministic.md)
- [Tapes holding words and configurations of such tapes](wordscfg.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/OutputToTape.lean)
