---
declaration: section
origin: cited
lean: Cslib.SessionTypes.SingleChannel, Cslib.SessionTypes.SingleChannel.dual, Cslib.SessionTypes.SingleChannel.advance, Cslib.SessionTypes.HasType.eq_nil_of_completed, Cslib.SessionTypes.SingleChannel.active_eq, Cslib.SessionTypes.HasType.send_shape, Cslib.SessionTypes.HasType.recv_shape, Cslib.SessionTypes.progress
statement: formalized
proof: formalized
---

# Progress and completion for isolated finite binary sessions

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html).

## Single active channel condition for a session context

All active obligations of this thread belong to one physical channel.

Formalized by `Cslib.SessionTypes.SingleChannel`, a definition declared in [CSLibExt/Languages/SessionTypes/Progress.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Progress.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html#single-channel).

## Dual context keeps the single active channel

Opposite roles have the same active-channel support.

Formalized by `Cslib.SessionTypes.SingleChannel.dual`, a theorem declared in [CSLibExt/Languages/SessionTypes/Progress.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Progress.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html#dual).

## Advancing the sole channel keeps the single-channel condition

Communication on the sole session cannot create another dependency.

Formalized by `Cslib.SessionTypes.SingleChannel.advance`, a theorem declared in [CSLibExt/Languages/SessionTypes/Progress.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Progress.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html#advance).

## Typed thread with completed obligations is nil

A typed thread whose endpoint obligations are completed is inert.

Formalized by `Cslib.SessionTypes.HasType.eq_nil_of_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Progress.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Progress.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html#eq-nil-of-completed).

## The only active channel is the designated one

Every active endpoint of a single-channel thread is the designated one.

Formalized by `Cslib.SessionTypes.SingleChannel.active_eq`, a theorem declared in [CSLibExt/Languages/SessionTypes/Progress.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Progress.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html#active-eq).

## Send obligation on the sole channel forces an output guard

A send obligation forces a send guard on the sole active channel.

Formalized by `Cslib.SessionTypes.HasType.send_shape`, a theorem declared in [CSLibExt/Languages/SessionTypes/Progress.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Progress.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html#send-shape).

## Receive obligation on the sole channel forces an input guard

A receive obligation forces an input guard on the sole active channel.

Formalized by `Cslib.SessionTypes.HasType.recv_shape`, a theorem declared in [CSLibExt/Languages/SessionTypes/Progress.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Progress.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html#recv-shape).

## Progress for dual single-channel session threads

Dual single-channel threads have either completed or can synchronize.
The single-channel hypothesis excludes cross-session dependency cycles.

Formalized by `Cslib.SessionTypes.progress`, a theorem declared in [CSLibExt/Languages/SessionTypes/Progress.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Progress.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html#progress).

## Completed sole protocol means both threads are nil

A completed sole protocol means both threads have reached `nil`.

Formalized by `Cslib.SessionTypes.BinaryTyped.completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Progress.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Progress.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html#completed).

## Session communication paths are π-calculus reduction paths

Paths of session communication are paths of existing π reductions.

Formalized by `Cslib.SessionTypes.represent_steps`, a theorem declared in [CSLibExt/Languages/SessionTypes/Progress.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Progress.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html#represent-steps).

## Finite completion of isolated finite binary sessions

Every isolated finite dual session admits a finite communication path to
completion. This excludes recursion and is not global π normalization.

Formalized by `Cslib.SessionTypes.finite_completion`, a theorem declared in [CSLibExt/Languages/SessionTypes/Progress.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Progress.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html#finite-completion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Progress and completion for isolated finite binary sessions](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/session-types/finite-binary-sessions/progress-and-completion-for-isolated-finite-bina)
