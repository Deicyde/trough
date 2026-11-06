# Adeles

We finish this miniproject by proving some results about Haar characters for algebras over adele rings. So let $K$ be a number field and let $\mathbb{A}_K$ be the adeles of $K$. We will prove some theorems about $\mathbb{A}_K$-algebras $R$ which are finite and free as $\mathbb{A}_K$-modules. Such algebras can be given the $\mathbb{A}_K$-module topology and this makes them into locally compact topological rings. In fact we shall only be concerned in applications with algebras of the form $B\otimes_K\mathbb{A}_K$ where $B$ is a finite-dimensional $K$-algebra. So fix such a $B$, and write $B_{\mathbb{A}}$ for $B\otimes_K\mathbb{A}_K$. Let us first deal with a subtlety. Recall that if $K\subseteq L$ are number fields, then $\mathbb{A}_L$ is a module-finite $\mathbb{A}_K$-algebra and hence an $\mathbb{A}_K$-module, and theorem [NumberField.AdeleRing.baseChange\_moduleTopology](../../miniproject-adeles/base-change/part-02/numberfield-adelering-basechange-moduletopology.md) tells us that $\mathbb{A}_L$ has the $\mathbb{A}_K$-module topology. Thus the next lemma applies.

- [IsModuleTopology.continuous\_bilinear\_of\_finite\_left](ismoduletopology-continuous-bilinear-of-finite-l.md)
- [NumberField.AdeleRing.ModuleBaseChangeContinuousLinearEquiv](numberfield-adelering-modulebasechangecontinuous.md)

As a consequence, if $B$ is a $K$-algebra then we can think of $B_{\mathbb{A}}$ as either $B\otimes_K\mathbb{A}_K$ with the $\mathbb{A}_K$-module topology or as $B\otimes_{\mathbb{Q}}\mathbb{A}_{\mathbb{Q}}$ with the $\mathbb{A}_{\mathbb{Q}}$-module topology. Note that this isomorphism commutes with the inclusions from $B$ into these rings. But Lean is picky about these things so we'll have to be careful.

- [NumberField.AdeleRing.isCentralSimple\_addHaarScalarFactor\_left\_mul\_eq\_right\_mul](numberfield-adelering-iscentralsimple-addhaarsca.md)

The previous theorem only applies to inner forms of matrix algebras, but the below theorem, a generalization of the adelic product formula, is valid for any finite-dimensional $K$-algebra. Before we state it let's remind ourselves of the product formula for $\mathbb{Q}$, and restate it in the language of these Haar characters.

- [MeasureTheory.ringHaarChar\_adeles\_rat](measuretheory-ringhaarchar-adeles-rat.md)

Now $\mathbb{A}_{\mathbb{Q}}$ is nonzero a $\mathbb{Q}$-algebra and hence we have an inclusion $\mathbb{Q}^\times\to\mathbb{A}_{\mathbb{Q}}^\times$. Here is our reinterpretation of the product formula.

- [MeasureTheory.ringHaarChar\_adeles\_units\_rat\_eq\_one](measuretheory-ringhaarchar-adeles-units-rat-eq-o.md)

Next we generalize this to finite-dimensional $\mathbb{Q}$-vector spaces.

So say $V$ is an $N$-dimensional $\mathbb{Q}$-vector space, and define $V_{\mathbb{A}}:= V\otimes_{\mathbb{Q}}\mathbb{A}_{\mathbb{Q}}$ with its $\mathbb{A}_{\mathbb{Q}}$-module topology. If we choose an isomorphism $V\cong\mathbb{Q}^N$ then $V_{\mathbb{A}}\cong\mathbb{A}_{\mathbb{Q}}^N$ as an additive topological abelian group. In particular, $V_{\mathbb{A}}$ is locally compact.

Fix a $\mathbb{Q}$-linear automorphism $\phi:V\to V$. By base extension $\phi$ induces an $\mathbb{A}_{\mathbb{Q}}$-linear automorphism $\phi_{\mathbb{A}}$ of $V_{\mathbb{A}}$ which is also a homeomorphism of $V_{\mathbb{A}}$ if $V_{\mathbb{A}}$ is given the module topology as an $\mathbb{A}_{\mathbb{Q}}$-module. Our goal is

- [MeasureTheory.addHaarScalarFactor\_tensor\_adeles\_eq\_one](measuretheory-addhaarscalarfactor-tensor-adeles.md)
- [NumberField.AdeleRing.units\_mem\_ringHaarCharacter\_ker](numberfield-adelering-units-mem-ringhaarcharacte.md)
- [NumberField.AdeleRing.addEquivAddHaarChar\_mulRight\_unit\_eq\_one](numberfield-adelering-addequivaddhaarchar-mulrig.md)
