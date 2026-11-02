# Local compactness

As mentioned above, Salvatore Mercuri was the first to give a complete formalisation of the proof that the adele ring is locally compact as a topological space. His work is in [his own repo](https://github.com/smmercuri/adele-ring_locally-compact) and proved the result using the “ad hoc” topology on the adeles which we initially had. Since then, adeles have been refactored to have the direct limit topology and mathlib has [RestrictedProduct.locallyCompactSpace\_of\_addGroup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/RestrictedProduct.html#RestrictedProduct.locallyCompactSpace_of_addGroup), the result that a restricted product of topological additive groups $K_v$ over compact open subgroups $A_v$ is locally compact.

What we need then is this (note that this is not true for a general Dedekind domain):

- [NumberField.instCompactSpaceAdicCompletionIntegers](numberfield-instcompactspaceadiccompletionintege.md)
- [NumberField.AdeleRing.locallyCompactSpace](numberfield-adelering-locallycompactspace.md)
