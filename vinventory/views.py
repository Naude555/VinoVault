from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Wine


class WineListView(LoginRequiredMixin, ListView):
    """
    Display a list of wines in the inventory.
    """

    model = Wine
    template_name = "vinventory/wine_list.html"
    context_object_name = "wines"

    def get_queryset(self):
        """
        Return the wines filtered by the logged-in user.
        """
        return Wine.objects.filter(user=self.request.user)

    def get_success_url(self):
        """
        Return the URL to redirect to after successful operations.
        """
        return reverse_lazy("vinventory:wine_list")

    def drink_wine(self, pk):
        """
        Decrease the quantity of a wine and save the changes.
        """
        wine = Wine.objects.get(pk=pk)
        if wine.quantity > 0:
            wine.quantity -= 1
            wine.save()
        return HttpResponseRedirect(
            self.request.META.get("HTTP_REFERER", "/")
        )  # Redirect back to the same page

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests, including the 'drink' action.
        """
        if "drink" in request.POST:
            wine_pk = request.POST.get("wine_pk")
            self.drink_wine(wine_pk)
        return self.get(request, *args, **kwargs)


class WineCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new wine entry in the inventory.
    """

    model = Wine
    template_name = "vinventory/wine_form.html"
    fields = [
        "name",
        "variety",
        "region",
        "year",
        "quantity",
        "received_from",
        "date_received",
        "date_to_drink_start",
        "date_to_drink_end",
    ]

    def form_valid(self, form):
        """
        Set the current user as the owner of the new wine entry.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        Return the URL to redirect to after successful creation.
        """
        return reverse_lazy("vinventory:wine_list")


class WineUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update an existing wine entry in the inventory.
    """

    model = Wine
    template_name = "vinventory/wine_form.html"
    fields = [
        "name",
        "variety",
        "region",
        "year",
        "quantity",
        "received_from",
        "date_received",
        "date_to_drink_start",
        "date_to_drink_end",
    ]

    def get_queryset(self):
        """
        Return the wines filtered by the logged-in user.
        """
        return Wine.objects.filter(user=self.request.user)

    def get_success_url(self):
        """
        Return the URL to redirect to after successful update.
        """
        return reverse_lazy("vinventory:wine_list")


class WineDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a wine entry from the inventory.
    """

    model = Wine
    template_name = "vinventory/wine_confirm_delete.html"
    success_url = reverse_lazy("vinventory:wine_list")

    def get_queryset(self):
        """
        Return the wines filtered by the logged-in user.
        """
        return Wine.objects.filter(user=self.request.user)

    def get_success_url(self):
        """
        Return the URL to redirect to after successful deletion.
        """
        return reverse_lazy("vinventory:wine_list")
